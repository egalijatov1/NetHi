### Clustering imports
from sklearn.cluster import AgglomerativeClustering
from networkx.algorithms import community
import itertools

### Other imports
import pandas as pd
import networkx as nx
import numpy as np
from collections import Counter
from scipy import stats
import math



def data_preprocess(data):
    # for col in data.columns:
    #     data = data.loc[data[col] != "Null"]
    #
    # """Checks for each column, if it contains a null element, if yes, it removes it from the dataset"""
    #
    # if(len(data)>15000):
    #     data = data.sample(n=15000)

    return(data)

def createGraph(data,s,t):
    ### Edge Atrr might be a problem True or non,
    if data.shape[1]>2:
        graph = nx.from_pandas_edgelist(data, source=s, target=t,edge_attr=True)
    else:
        graph = nx.from_pandas_edgelist(data, source=s, target=t,edge_attr=None)

    """Source and target will be input parameters that the user will give, and we'll give them to the function
     that creates the graph"""
    graph = graph.to_undirected() #Louvain only works with undirected graphs
    return graph

### PRINTS GRAPH INFO
def graph_info(graph):
    # TWO PANDAS SERIES OF STRINGS AND THE RESULTS ARE CREATED AND SENT AS DATAFRAME
    degrees = [val for (node, val) in graph.degree()]
    listcol1 = ["Number of nodes ","Number of edges ","Maximum degree ","Minimum degree ","Average degree ",
                "Most frequent degree ","Density ","Number of selfloops ","Degree assortiativity coefficient "]
    column1 = pd.Series(listcol1)
    listcol2 = [str(len(graph.nodes)),str(len(graph.edges)), str(np.max(degrees)),str(np.min(degrees)),str(np.round(np.mean(degrees),6)),
                str(stats.mode(degrees)[0][0]),str(round(nx.density(graph),6)),str(nx.number_of_selfloops(graph)),
                str(round(nx.degree_assortativity_coefficient(graph), 6))]
    column2 = pd.Series(listcol2)
    return pd.concat([column1, column2], axis=1)

### CALCULATES THE PAGE RANK FOR EACH NODE AND DISPPLAYS THE TOP N
def pagerank_calc(graph,n):
    page_rank = nx.pagerank_scipy(graph)
    """top n nodes along with their page rank value"""
    highest_page_rank_dict = sorted(page_rank.items(), key=lambda kv: kv[1], reverse=True)[:n]
    """top n nodes only as a list of node names"""
    highest_page_rank_nodes = sorted(page_rank, key=page_rank.get, reverse=True)[:n]
    return(page_rank,highest_page_rank_dict,highest_page_rank_nodes)

def community_clustering_info(partition,graph):
    number_of_communities = len(list(set([i for i in partition.values()])))
    communities_members = Counter(partition.values())
    communities = [[] for c in range(0,number_of_communities)]
    for k in partition.keys():
        communities[partition[k]].append(k)

    col1=["Number of communities detected",  "Largest community (id)", "Size of largest community", "Smallest community (id)",
          "Size of smallest community", "Modularity of partition"]
    col1=pd.Series(col1)
    col2=[str(number_of_communities), str(Counter(communities_members).most_common(1)[0][0]),
         str(Counter(communities_members).most_common(1)[0][1]), str(communities_members.most_common()[:-1 - 1:-1][0][0]),
         str(communities_members.most_common()[:-1 - 1:-1][0][1]), str(round(community.modularity(graph, communities), 6))]
    col2=pd.Series(col2)
    return pd.concat([col1, col2], axis=1)

def _position_nodes(g, partition, **kwargs):
    """
    Positions nodes within communities.
    """

    communities = dict()
    for node, community in partition.items():
        try:
            communities[community] += [node]
        except KeyError:
            communities[community] = [node]

    pos = dict()
    for ci, nodes in communities.items():
        subgraph = g.subgraph(nodes)
        pos_subgraph = nx.spring_layout(subgraph, **kwargs)
        pos.update(pos_subgraph)

    return pos

def _find_between_community_edges(g, partition):

    edges = dict()

    for (ni, nj) in g.edges():
        ci = partition[ni]
        cj = partition[nj]

        if ci != cj:
            try:
                edges[(ci, cj)] += [(ni, nj)]
            except KeyError:
                edges[(ci, cj)] = [(ni, nj)]

    return edges

def _position_communities(g, partition, **kwargs):
    # create a weighted graph, in which each node corresponds to a community,
    # and each edge weight to the number of edges between communities
    between_community_edges = _find_between_community_edges(g, partition)

    communities = set(partition.values())
    hypergraph = nx.DiGraph()
    hypergraph.add_nodes_from(communities)
    for (ci, cj), edges in between_community_edges.items():
        hypergraph.add_edge(ci, cj, weight=len(edges))

    # find layout for communities
    pos_communities = nx.spring_layout(hypergraph,**kwargs)

    # set node positions to position of community
    pos = dict()
    for node, community in partition.items():
        pos[node] = pos_communities[community]

    return pos

def create_partition(graph, communities):
    partition = {}
    for node in graph.nodes:
        i = 0
        for c in communities:
            if node in c:
                partition[node] = i
                break
            i +=1
    return partition

def greedy(graph):
    c = list(nx.algorithms.community.modularity_max.greedy_modularity_communities(graph))
    partition = create_partition(graph, c)
    return partition,c

def louvain_community_detection(data_frame, attr1, attr2):
    data = data_preprocess(data_frame)
    graph = createGraph(data, attr1, attr2)
    num_nodes = len(graph.nodes)

    if num_nodes<51:
        number_of_important_nodes=10
    elif num_nodes<101:
        number_of_important_nodes=20
    elif num_nodes<501:
        number_of_important_nodes=50
    elif num_nodes<1001:
        number_of_important_nodes=100
    else:
        number_of_important_nodes = math.floor(num_nodes/50)
    all_nodes_pgrank, important_nodes_dict,important_nodes_list = pagerank_calc(graph,number_of_important_nodes)

    #partition = community.best_partition(graph)
    #partition = girvan_newman_community_detection(graph)
    partition, c = greedy(graph)
    print("modularity: ", nx.algorithms.community.quality.modularity(graph, c))
    print("coverage: ", nx.algorithms.community.quality.coverage(graph, c))


    pkc = 0
    scc = 0
    scn = 0
    if num_nodes <= 1000:
        scc = 5
        pkc = 0.2
        scn = 1
    else:
        scc = 40
        pkc = 1.
        scn = 2


    pos_communities = _position_communities(graph, partition, k=pkc, iterations=20, scale=scc)

    pos_nodes = _position_nodes(graph, partition, k=0.15, iterations=20, scale=scn)

    # combine positions
    pos2 = dict()
    for node in graph.nodes():
        pos2[node] = pos_communities[node] + pos_nodes[node]

    pos = {}
    for node_pos_key in pos2.keys():
        lat = (pos2[node_pos_key][0]+4)/4*1000
        long = (4 - pos2[node_pos_key][1])/4*1000
        pos[node_pos_key] = [lat, long]

    # Degrees of every node that will go in node info
    degrees = graph.degree() #
    node_list = []
    edge_list = []
    starting_elements = []

    #for node ids
    counter = 1

    #Calculate number of virtual nodes for each community
    count = len(list(set([i for i in partition.values()])))

    """ Add node information """
    #Adding main node
    main_node = {
        'data': {
            'id': 'main',
            'label': 'Graph Clusters',
            'hover_info':{
                    "node" : "Main node",
                    "text" : "Main node of the graph that connects community nodes",
                    "community" : ""
                },
            'community_id': 'main',
            'num_children': count #number of communities
        },
        'state':3,
        'expandable': True,
        'expanded': False,
        'classes': 'plus main important',
        'important': True,
        'position':{
            'x':1000,
            'y':1000
        }
    }

    node_list.append(main_node)
    starting_elements.append(main_node)

    #Computing mean position for each community virtual node
    latitudes = np.zeros(count)
    longitudes = np.zeros(count)
    community_count = np.zeros(count)
    for item in partition.items():
        latitudes[item[1]]+=pos[item[0]][0]
        longitudes[item[1]]+=pos[item[0]][1]
        community_count[item[1]]+=1
    latitudes = latitudes/community_count
    longitudes = longitudes/community_count

    #Adding virtual nodes
    for i in range(0, count):
        latitude = latitudes[i]
        longitude = longitudes[i]
        children = list(filter(lambda x: (x[1] == i), partition.items()))
        _children = []
        for item in children:
            _children.append(item[0])

        contains_important=False
        #Checks if community has an important node
        for item in important_nodes_list:
            if item in _children:
                contains_important = True

        node = {
            'data': {
                'id': 'virt'+str(i),
                'label': 'Community '+str(i+1),
                'hover_info': {
                    'node' : 'Virtual node',
                    'text': 'Virtual node of community '+str(i) +"\n\nNodes in community:",
                    'community': ""
                },
                'community_id': i,
                'num_children': len(list(filter(lambda x: (x[1] == i), partition.items())))
            },
            'expandable': True,
            'expanded': False,
            'state': 3,
            'classes':'plus '+str(i%100) + " important",
            'important': contains_important,
            'position':{
                'x': latitude,
                'y': longitude
            }
        }
        edge = {
            'data': {
                'source': 'main',
                'target': 'virt' + str(i),
                'edge_info': {
                    'text': 'Edge between main node and community ' + str(i),
                },
                'important': contains_important
            }
        }
        node_list.append(node)
        edge_list.append(edge)
        if contains_important:
            starting_elements.append(node)
            starting_elements.append(edge)


    # Adding regular nodes and edges to the virtual nodes
    for item in partition.items():
        important = item[0] in important_nodes_list
        latitude = pos[item[0]][0]
        longitude = pos[item[0]][1]
        style_class = str(item[1]%100)
        label = ""
        if important:
            style_class += " important"
            label = str(item[0])
        node = {
            'data': {
                'id': str(counter),
                'label': label,
                'hover_info':{
                    "node" : "Node: " + str(item[0]),
                    "text" : "Degree: " + str(degrees[item[0]]) + "\n\nPage Rank: " + str(round(all_nodes_pgrank[item[0]],4)),
                    "community" : "Community ID: " + str(item[1])
                },
                'community_id': item[1],
                'num_children': 0
            },
            'expandable':False,
            'classes': style_class,
            'important': important,
            'position':{
                'x': latitude,
                'y': longitude
            }
        }
        edge= {
            'data':{
                'source':'virt'+str(item[1]),
                'target': str(counter),
                'edge_info': {
                    'text': 'Edge information',
                },
                'important': important
            }
        }
        node_list.append(node)
        edge_list.append(edge)
        node_list[item[1]+1]['data']['hover_info']['text']+= "\n  - "+str(item[0])
        if important:
            starting_elements.append(node)
            starting_elements.append(edge)
        counter = counter + 1

    clustering_report = community_clustering_info(partition,graph)
    graph_report = graph_info(graph)
    return node_list,edge_list, starting_elements, clustering_report, graph_report


def preprocess_agglomerative(data, attrs):
    data_new = data[attrs]
    return (data_new)

def agglomerative_clustering_info(data, clusters):
    column1 = ["Number of clusters", "Biggest cluster (id)","Number of samples in biggest cluster", "Smallest cluster (id)",
               "Number of samples in smallest cluster"]
    cnt = Counter(clusters)
    column2 = [str(len(list(set(clusters)))),str(cnt.most_common(1)[0][0]),
               str(cnt.most_common(1)[0][1]),str(cnt.most_common()[:-1 - 1:-1][0][0]),
               str(cnt.most_common()[:-1 - 1:-1][0][1])]

    return pd.concat([pd.Series(column1), pd.Series(column2)], axis=1)


def agglomerative_clustering(data_frame, attrs, num_clusters=3):

    flag = True

    """This code checks if the first attribute chosen is of a column with ids/names or just regular values for the cluster
    algorithm. If they are numeric, means the user did not select an id attribute to name the instances, so we assign a 
    counter that will make a list of names for each instance(leaf in the dendogram)"""

    for item in data_frame[attrs[0]]:
        if not(type(item) == int or type(item) == float):
            flag = False

    labels = []
    if flag:
        for i in range(0, len(data_frame[attrs[0]])):
            labels.append("Leaf: " + str(i))
    else:
        #Will use this to name the leaves
        for item in data_frame[attrs[0]]:
            labels.append(item)

    attributes = []
    if flag:
        attributes = attrs
    else:
        for i in range(1,len(attrs)):
            attributes.append(attrs[i])
    data = data_frame[attributes]

    node_list = []
    edge_list = []
    starting_elements = []

    X = data
    y = labels
    model = AgglomerativeClustering(distance_threshold = None, n_clusters = num_clusters)
    model.fit(X)
    clusters = model.fit(X).labels_

    node_clust = {}
    node_num_children = {}
    node_children_names = {}
    id_label_list = {}
    ii = itertools.count(X.shape[0])

    res = [{'node_id': next(ii), 'left': x[0], 'right': x[1]} for x in model.children_]

    for i in range(0,X.shape[0]):
        style_class = str(clusters[i])
        label = str(y[i])
        text = "Attributes:\n"

        #add attribute values to node info
        for attr in list(X.columns.values):
            text += "  " + attr + ": " + str(X[[attr]].iloc[[i]].values[0][0])  + "\n"

        node = {
            'data':{
                'id': str(i),
                'label': label,
                'hover_info': {
                    'node' : label,
                    'text': text,
                    'community': 'Cluster id: ' + str(clusters[i])
                },
                'community_id': clusters[i],
                'num_children': 0
            },
            'expandable': False,
            'classes': style_class,
            'important': False
        }
        node_list.append(node)

        node_clust[str(i)] = clusters[i]
        node_num_children[str(i)] = 0
        node_children_names[str(i)] = ""
        id_label_list[str(i)] = label


    num_leafs = X.shape[0]  #for graph info
    counter = len(res)-1
    num_nodes = 0 #for graph info

    for edge in res:
        id = edge['node_id']
        left_child = edge['left']
        right_child = edge['right']

        if str(left_child) not in node_clust:
            left_child = 'main' + str(left_child)
        if str(right_child) not in node_clust:
            right_child = 'main' + str(right_child)

        if node_clust[str(left_child)] == node_clust[str(right_child)]:

            if str(left_child).startswith('m') or str(right_child).startswith('m'):
                id_x = 'main' + str(id)
            else:
                id_x = str(id)
            node_clust[id_x] = node_clust[str(left_child)]
        else:
            id_x = 'main'+str(id)
            node_clust[id_x] = 'main'

        node_label=''
        if node_clust[id_x] == 'main':
            node_label = 'Main node'
        else:
            node_label = 'Sub cluster node'


        counter=counter-1

        style_class = str(node_clust[id_x]) + " plus"

        #number of children
        num_ch = node_num_children[str(left_child)] + node_num_children[str(right_child)] + 2
        node_num_children[id_x] = num_ch

        if counter == -1:
            num_nodes=num_ch

        #chlidren names
        ch_names = ""
        if node_children_names[str(left_child)] != "":
            ch_names += node_children_names[str(left_child)]
        if node_children_names[str(right_child)] != "":
            ch_names += node_children_names[str(right_child)]
        if id_label_list[str(left_child)] != "":
            ch_names += "\n" + id_label_list[str(left_child)]
        if id_label_list[str(right_child)] != "":
            ch_names += "\n" + id_label_list[str(right_child)]
        node_children_names[id_x] = ch_names

        id_label_list[id_x] = ""

        sorted_ch_names = ch_names.splitlines()
        sorted_ch_names.sort()
        ch_names = ""
        for x in sorted_ch_names:
            if x!="":
                ch_names += "\n  - " + x

        node = {
            'data': {
                'id': id_x,
                'label': "",
                'hover_info': {
                    'node' : node_label,
                    'text': 'Number of child nodes: ' + str(num_ch) + "\n\nChild leaf nodes (" + str(len(sorted_ch_names)-1) + "): " + ch_names,
                    'community' : "Cluster id: " + str(node_clust[id_x])
                },
                'community_id': node_clust[id_x],
                'num_children': num_ch
            },
            'expandable': True,
            'expanded': False,
            'classes': style_class,
            'important': False
        }
        node_list.append(node)

        left_edge = {
            'data': {
                'source': id_x,
                'target': str(left_child),
                'edge_info': {
                    'text': 'Edge information',
                }
            },
            'classes': str(node_clust[str(left_child)]) + 'e',
            'important': False
        }

        right_edge = {
            'data': {
                'source': id_x,
                'target': str(right_child),
                'edge_info': {
                    'text': 'Edge information',
                }
            },
            'classes': str(node_clust[str(right_child)]) + 'e',
            'important': False
        }

        edge_list.append(left_edge)
        edge_list.append(right_edge)

    if num_nodes <= 63:
        starting_elements = node_list + edge_list
    else:
        curr_nodes = node_list[-1:]
        ctr = 0

        for i in range(0,63):
            node = curr_nodes[0]
            edges = list(filter(lambda x: (x['data']['source'] == node['data']['id']), edge_list))
            for edge in edges:
                curr_nodes += list(filter(lambda x: x['data']['id'] == edge['data']['target'], node_list))
            if(i < 31):
                if node['expandable'] and not node['data']['id'].startswith('m'):
                    node['expanded'] = True
                    node['classes'] = "minus " + str(node['data']['community_id'] % 100)
                if node['data']['id'].startswith('m'):
                    node['classes'] = "minus main"
            else:
                if node['expandable'] and not node['data']['id'].startswith('m'):
                    node['expanded'] = False
                    node['classes'] = "plus " + str(node['data']['community_id'] % 100)
                if node['data']['id'].startswith('m'):
                    node['classes'] = "plus main"
            starting_elements.append(curr_nodes[0])
            starting_elements += edges
            curr_nodes.pop(0)
            i+=1


    cluster_report = agglomerative_clustering_info(data,clusters)
    graph_report_col1 = ["Total number of nodes ", "Number of leafs", "Number of cluster nodes"]
    graph_report_col2 = [str(num_nodes),str(num_leafs),str(num_nodes-num_leafs)]
    graph_report = pd.concat([pd.Series(graph_report_col1),pd.Series(graph_report_col2)],axis=1)
    return node_list, edge_list, starting_elements, cluster_report, graph_report


