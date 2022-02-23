import dash
from dash.dependencies import Input, Output, State
from dash import html
import dash_cytoscape as cyto
import pandas as pd
import numpy as np
from dash import dash_table as dt
import dash_bootstrap_components as dbc
import copy
import layout
from model_manipulation import louvain_community_detection
from model_manipulation import agglomerative_clustering
import base64
import io


no_clicks_visualize = 0
no_clicks_expand = 0
data_frame = None

nodes = []
edges = []
starting_elements = []

graph_report = pd.DataFrame()
cluster_report = pd.DataFrame()

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
cyto.load_extra_layouts()

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

"load attributes based on file contents"
def loadAttributes(data):
    list_of_attrs = []
    i = 0

    for col in data.columns:
         list_of_attrs.append({
             'label': col,
             'value': col
         })
         i += 1
    return list_of_attrs

#true if elements contain node
def contains_node(id, elements):
    for element in elements:
        if element['data']['id'] == id:
            return True
    return False

"""add important nodes"""
def add_important_children(id,elements):
    child_ids = []
    child_nodes = []
    child_edges = []
    for edge in edges:
        if edge['data']['source'] == id:
            if len(list(filter(lambda x: (x['data']['id'] == edge['data']['target']), elements))) == 0:
                child_ids.append(edge['data']['target'])
                child_edges.append(edge)
    for ch in child_ids:
        for node in nodes:
            if node['data']['id'] == ch and node['important']:
                node['classes'] =  str(node['data']['community_id']%100)
                if node['expandable'] == True:
                    node['expanded'] = False
                    if node['important']:
                        node['classes'] += ' star'
                        node['state']=2
                    else:
                        node['classes'] += ' plus'
                        node['state']=3
                if node['important']:
                    node['classes'] += " important"
                #print(node['classes'])
                child_nodes.append(node)

    return child_nodes+child_edges

"""adding children nodes"""
def add_children(id, elements):
    child_ids = []
    child_nodes = []
    child_edges = []
    for edge in edges:
        if edge['data']['source'] == id:
            if len(list(filter(lambda x: (x['data']['id'] == edge['data']['target']), elements))) == 0:
                child_ids.append(edge['data']['target'])
                child_edges.append(edge)
    for ch in child_ids:
        for node in nodes:  
            if node['data']['id'] == ch:  
                node['classes'] =  str(node['data']['community_id']%100)
                if node['expandable'] == True:
                    node['expanded'] = False
                    if node['important']:
                        node['classes'] += ' star'
                        node['state']=2
                    else:
                        node['classes'] += ' plus'
                        node['state']=3
                if node['important']:
                    node['classes'] += " important"
                child_nodes.append(node)
    return child_nodes+child_edges

"""removing children nodes"""
def remove_children(id, elements):
    children = []
    remove_branches = []
    removed_nodes = []
    for element in elements:
        source =""
        try:
            source = element['data']['source']
        except:
            source = ""
        if source == id:
            children.append(element['data']['target'])
            remove_branches.append(element)

    for branch in remove_branches:
        elements.remove(branch)

    for ch in children:
        for element in elements:
            if element['data']['id'] == ch:
                elements = remove_children(ch, elements)
                removed_nodes.append(element['data']['id'])
                elements.remove(element)
    return elements

def do_clustering(alg, attrs, no_of_clusters):
    global nodes
    global edges
    global graph_report
    global cluster_report
    global starting_elements
    if alg ==  '1':
        nodes, edges, starting_elements, cluster_report, graph_report = louvain_community_detection(data_frame, attrs[0], attrs[1])
    elif alg == '2':
        nodes, edges, starting_elements, cluster_report, graph_report = agglomerative_clustering(data_frame,attrs, no_of_clusters)
    starting_elements = copy.deepcopy(starting_elements)
    return

def set_elements():
    ret = {'elements': starting_elements, 'report': graph_report}
    return ret


search_bar=dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button("Search", color="primary", className="ml-2 btn-primary"),
            width="auto",
        ),
    ],
    # no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center"
)
app.layout = layout.app_layout


"""save file contents into data_frame"""
@app.callback([Output('dataset_name', 'children'),
               Output('atrSelection', 'options'),
               Output('atrSelection', 'value')],
              [Input('upload-data', 'contents'),
              Input('upload-data', 'filename')])
def process_file(contents, filename):
    if contents==None:
        return "No dataset uploaded!", [], None
    content_string = contents.split(',')
    decoded = base64.b64decode(content_string[1])

    #save file contents into dataframe
    global data_frame
    data_frame = pd.read_csv(io.StringIO(decoded.decode('utf-8')))

    #load attributes into dropdown

    atr = loadAttributes(data_frame)
    return "DATASET: " + str(filename), atr, None

"""save alg_selection value"""
@app.callback([Output('laySelection', 'value'),
               Output('laySelection', 'options'),
               Output('legend','children'),
               Output('no_of_clusters', 'style'),
               Output('note_text', 'style')],
              [Input('algSelection', 'value')])
def save_alg_selection(value):
    if value == None:
        return [], 'cose', {'display':'none', 'background-color' : '#F5F5F5',}, {'display':'none'}
    elif value == '1':
        options = [
            {'label': name, 'value': val}
            for name, val in [['Preset (recommended)', 'preset'], ['Breadthfirst', 'breadthfirst'],
                              ['Cose', 'cose'], ['Dagre', 'dagre'], ['Spread', 'spread']]
        ]
        children=layout.legendLouvain
        style = {'display':'none',
                 'background-color' : '#F5F5F5',
                 }
        return 'preset', options,children, style, {'display':'none'}
    else:
        options = [
            {'label': name, 'value': val}
            for name, val in [['Preset', 'preset'], ['Breadthfirst', 'breadthfirst'],
                              ['Cose', 'cose'], ['Dagre (recommended)', 'dagre'], ['Spread', 'spread']]
        ]
        children=layout.legendAglomerative
        style = {'display': 'block',
                 'background-color' : '#F5F5F5',
                 }
        return 'dagre', options, children, style, {'display':'block'}


"""Save atr_selection value"""
@app.callback([Output('error_attr_label','style'),
               Output('error_attr_label2','style'),
               Output('error_attr_label3','style')],
              [Input('atrSelection', 'value')],
               [State('algSelection', 'value')])
def save_atr_selection(value, algSelection):
    if value != None:
        if algSelection == '1' and len(value) != 2:
            return {'display':'block', 'color': '#FF0000'}, \
                   {'display':'none', 'color': '#FF0000'},\
                   {'display':'none', 'color': '#FF0000'}
        elif algSelection == '2' and len(value)!=0:
            i = 0
            for col_name in value:
                if i != 0 and not np.issubdtype(data_frame.dtypes[col_name], np.number):
                    return {'display':'none', 'color': '#FF0000'}, \
                           {'display':'none', 'color': '#FF0000'},\
                           {'display':'block', 'color': '#FF0000'}
                i+=1
            return {'display':'none', 'color': '#FF0000'}, \
                   {'display':'none', 'color': '#FF0000'},\
                   {'display':'none', 'color': '#FF0000'}
        elif algSelection == '2' and len(value) == 0:
            return {'display':'none', 'color': '#FF0000'}, \
                   {'display':'block', 'color': '#FF0000'},\
                   {'display':'none', 'color': '#FF0000'}
        else:
            return {'display':'none', 'color': '#FF0000'}, \
                   {'display':'none', 'color': '#FF0000'},\
                   {'display':'none', 'color': '#FF0000'}
    else:
        return {'display':'none', 'color': '#FF0000'}, \
               {'display':'none', 'color': '#FF0000'},\
               {'display':'none', 'color': '#FF0000'}

"""do clustering and save report to results"""
@app.callback([Output('clust-results-table', 'children'),
               Output('graph-report-table','children'),
               Output('error_cluster_label','style'),
               Output('error_attributes_label','style'),
               Output('error_no_of_clusters','style')],
              [Input('cluster','n_clicks')],
               [State('no_of_clusters','value'),
               State('algSelection', 'value'),
                State('atrSelection','value')]
             )
def clustering(n_clicks,no_of_clusters, alg_name, attributes):
    global data_frame
    if n_clicks == None:
        return "", "", {'display':'none', 'color': '#FF0000'}, {'display':'none', 'color': '#FF0000'}, {'display':'none', 'color': '#FF0000'}
    else:
        if not(data_frame is not None) or data_frame.empty:
            return "","", {'display':'block', 'color': '#FF0000'}, {'display':'none', 'color': '#FF0000'}, {'display':'none', 'color': '#FF0000'}

        if isinstance(no_of_clusters,int)==False or no_of_clusters<1 or no_of_clusters==None:
            return "", "", {'display':'none', 'color': '#FF0000'}, {'display':'none', 'color': '#FF0000'},{'display':'block', 'color': '#FF0000'}

        if attributes != 'null' and attributes != "" and attributes != None and not len(attributes)==0:
            do_clustering(alg_name, attributes,no_of_clusters)
            mycolumns = [{'name': i, 'id': i} for i in graph_report.columns]
            mycolumns_clust = [{'name': i, 'id': i} for i in cluster_report.columns]
            ret1 = html.Div([
                dt.DataTable(
                    id='clust-results-table',
                    columns=mycolumns_clust,
                    style_as_list_view=True,
                    style_cell={'textAlign': 'left'},
                    style_header={
                        'display': 'none'
                    },
                    style_data_conditional=[
                        {
                            'if': {'row_index': 'odd'},
                            'backgroundColor': 'rgb(230,230,250)'
                        }
                    ],
                    data=cluster_report.to_dict("rows")),
            ])
            ret2 = html.Div([
                dt.DataTable(
                    id = 'graph-report-table',
                    columns = mycolumns,
                    style_as_list_view = True,
                    style_table = {

                    },
                    style_cell={'textAlign': 'left'},
                    style_header={
                        'display' : 'none'
                    },
                    style_data_conditional=[
                        {
                            'if': {'row_index': 'odd'},
                            'backgroundColor': 'rgb(230,230,250)'
                        }
                    ],
                    data=graph_report.to_dict("rows")),
                    ])

            return ret1, ret2, {'display':'none', 'color': '#FF0000'}, {'display':'none', 'color': '#FF0000'}, {'display':'none', 'color': '#FF0000'}
        else:
            return "","", {'display':'none', 'color': '#FF0000'}, {'display':'block', 'color': '#FF0000'}, {'display':'none', 'color': '#FF0000'}


"""Change layout"""
@app.callback(Output('visualization', 'layout'),
              [Input('laySelection', 'value')],
              [State('visualization', 'elements')])
def update_layout(layout, elements):
    return {
        'name': layout,
        'animate': True
    }


"""Visualization callback"""
@app.callback([Output('visualization', 'elements'),
               Output('do_clustering_label','style')],
              [Input('visualization', 'tapNode'),
               Input('visualize', 'n_clicks'),
               Input('expand','n_clicks')],
              [State('visualization', 'elements'),
               State('clust-results-table', 'children')])
def node_interaction(nodeTap,n_clicks_vis, n_clicks_exp, elements, clust):
    global no_clicks_visualize
    global no_clicks_expand
    global nodes
    global edges
    global starting_elements
    global graph_report
    global cluster_report
    global data_frame

    #first pass when app is loaded - restart all global variables
    if nodeTap == None and n_clicks_exp == None and n_clicks_vis == None:
        no_clicks_visualize = 0
        no_clicks_expand = 0
        data_frame = None

        nodes = []
        edges = []
        starting_elements = []

        graph_report = pd.DataFrame()
        cluster_report = pd.DataFrame()
        return [],{'display':'none', 'color': '#FF0000'}

    #visualize button is clicked
    elif n_clicks_vis!= None and n_clicks_vis > no_clicks_visualize:
        no_clicks_visualize += 1
        if len(starting_elements) == 0:
            return [], {'display':'block', 'color': '#FF0000'}
        return starting_elements, {'display':'none', 'color': '#FF0000'}

    #expand button is clicked
    elif n_clicks_exp != None and n_clicks_exp > no_clicks_expand:
        no_clicks_expand+=1
        if len(nodes) == 0:
            return [], {'display': 'block', 'color': '#FF0000'}
        for node in nodes:
            if node['expandable'] and not node['data']['id'].startswith('m'):
                node['expanded'] = True
                node['classes'] = "minus " + str(node['data']['community_id']%100)
            if node['data']['id'].startswith('m'):
                node['classes'] = "minus main"
            if node['important']:
                node['classes'] += ' important'
        return nodes+edges, {'display':'none', 'color': '#FF0000'}

    if len(nodes) == 0:
        return [], {'display':'block', 'color': '#FF0000'}

    #node is clicked
    nodeData = nodeTap['data']
    for element in elements:
        if nodeData['id'] == element.get('data').get('id'):

            
            #do nothing if element is not expandable
            if element['expandable'] == False:
                return elements

            if 'state' in element:
                #state logic
                if element['state']==1:
                    ret = remove_children(nodeData['id'], elements)
                    if element['important']:
                        element['classes']="star "
                        element['state']=2
                    else:
                        element['classes']="plus "
                        element['state']=3
                elif element['state']==2:
                    ret=add_important_children(nodeData['id'], elements)
                    ret+=elements
                    element['classes']="plus "
                    element['state']=3
                elif element['state']==3:
                    ret=add_children(nodeData['id'], elements)
                    ret += elements
                    element['classes']="minus "
                    element['state']=1

                if str(element['data']['community_id']) != 'main':
                    element['classes']+=str(element['data']['community_id']%100)
                else:
                    element['classes'] += 'main'
                if element['important']:
                    element['classes'] += " important"
            else:    
                #if element is expanded colapse it
                if element['expanded'] == True:
                    expand = False
                    if str(element['data']['community_id']) != 'main':
                        element['classes'] = 'plus '+ str(element['data']['community_id']%100)
                    else:
                        element['classes'] = 'plus main'
                    if element['important']:
                        element['classes'] += " important"
                    element['expanded'] = False
                    ret = remove_children(nodeData['id'], elements)

                #if element is colapsed expand it
                else:
                    if element['data']['community_id']!='main':
                        element['classes'] = 'minus '+ str(element['data']['community_id']%100)
                    else:
                        element['classes'] = 'minus main'
                    if element['important']:
                        element['classes'] += " important"
                    element['expanded'] = True
                    children = add_children(nodeData['id'],elements)
                    ret = elements + children
                break     
    return ret,{'display':'none', 'color': '#FF0000'}


@app.callback([Output('node_label', 'children'),
               Output('node_cluster_info', 'children'),
               Output('node_text', 'children')],
              [Input('visualization', 'mouseoverNodeData')],)
def hover_node(nodeData):
    if nodeData:
        return nodeData['hover_info']['node'],nodeData['hover_info']['community'], nodeData['hover_info']['text']
    return "","",""


if __name__ == '__main__':
   app.run_server()