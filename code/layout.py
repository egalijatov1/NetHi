from dash import html
from PIL import Image
import dash_bootstrap_components as dbc
from dash import dcc
import dash_cytoscape as cyto
from stylesheet import default_stylesheet


plusImage = Image.open('images/plus.png')
minusImage = Image.open('images/minus.png')
starImage = Image.open('images/starr.png')
black_star = Image.open('images/star_black.png')
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"


my_stylesheet = default_stylesheet

app_layout= html.Div\
    (
        id = 'main_div',
        style={
            'background-color' : '#F5F5F5',
            'padding':'10px'
        },
        children =
        [
            dcc.Location(id='url', refresh=False),
            dbc.Navbar(
                [
                    html.A(
                            dbc.Row(
                            [
                                dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                                dbc.Col(dbc.NavbarBrand("NetHi", className="ml-2",
                                    style={
                                        'text-shadow' : '0.5px 0.5px #FFA500',
                                        'font-size': '30px',
                                        'color' : '#343a40'
                                })),
                                #dbc.Col(dbc.Nav(
                                #    [dbc.NavItem(dbc.NavLink("Exit", active=True, href="#"))],
                                #    pills=True,className="col-auto"),className="col-auto"),
                            ],
                            align="center",
                            # no_gutters=True,
                        ),
                        href="https://plot.ly",
                    ),
                    #dbc.NavbarToggler(id="navbar-toggler"),
                    #dbc.Collapse(search_bar, id="navbar-collapse", navbar=True), #TODO This can do search on the page through results
                ],
                color="#F5F5F5",
                #dark=True,
            ),
            html.H3(
                "A Tool for Exploring Communities in Interaction Networks and Cluster Visualization in Hierarchial Data",
                style={
                    'color' : '#343a40',
                    'margin-top' : '30px',
                    'textAlign' : 'center',
                    'marginBottom' : '60px',
                    #'color' : 'white',
                    #'font-style' : 'bold',
                    'font-family' : 'Arial, Gadget, sans-serif',
                    'line-height' : '50px',
                    'letter-spacing' : '-1.2px',
                    'word-spacing' : '1.6px'
                }
            ),

            dcc.Upload(
                id='upload-data',
                children=html.Div([
                    'Drag and Drop or ',
                    html.A("Select Files")
                ]),
                style={
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'marginBottom' : '15px',
                    'marginTop' : '15px',
                    'background-color' : "#F5F5F5",
                    'border-color' : '#343a40'
                }
            ),
            html.Div(id = 'dataset_name', children=["No dataset uploaded!"]),
            dcc.Dropdown(
                id="algSelection",
                placeholder = "Select clustering algorithm...",
                options=[
                    {"label": "Louvain Method", "value": "1"},
                    {"label": "Agglomerative Clustering", "value": "2"}
                ],
                style={
                    'marginBottom' : '15px',
                    'marginTop' : '15px',
                    'background-color': '#F5F5F5',
                    'color' : '#343a40',
                },
                value="1"
            ),
            html.Label(
                "NOTE: First attribute should have textual node label value, or ordinal numbers will be used.\n Other attributes must have numerical values!",
                id='note_text',
                style={
                    'display':'none',
                }
            ),
            dcc.Dropdown(
                id="atrSelection",
                placeholder = "Select attributes...",
                multi= True,
                style={
                    'marginBottom' : '15px',
                    'marginTop' : '15px',
                    'background-color' : '#F5F5F5',
                    'color' : '#343a40'
                }
            ),
            html.Label(
                "Please select 2 attributes!",
                id='error_attr_label',
                style={
                    'display':'none',
                    'color': '#FF0000'
                }
            ),
            html.Label(
                "Please select at least 1 attribute!",
                id='error_attr_label2',
                style={
                    'display':'none',
                    'color': '#FF0000'
                }
            ),
            html.Label(
                "Only first attribute can have textual value!",
                id='error_attr_label3',
                style={
                    'display':'none',
                    'color': '#FF0000'
                }
            ),
            dbc.Input(
                id = "no_of_clusters",
                type = "number",
                value=3,
                step = 1,
                min = 2,
                placeholder = "Number of clusters (2 or more)",
                style= {
                    'display':'none',
                    'background-color' : '#AAAAAA',
                    'color' : '#343a40'
                },

            ),
            dbc.Button("CLUSTER",
                    id = 'cluster',
                    color="primary",
                    className="btn-primary blue-gradient d-grid gap-2",
                    # block=True,
                    style={
                        'marginBottom' : '15px',
                        'marginTop' : '15px'
                }
            ),
            html.Label(
                "Upload dataset first!",
                id='error_cluster_label',
                style={
                    'display':'none',
                    'color': '#FF0000'
                }
            ),
            html.Label(
                "Choose attributes first!",
                id='error_attributes_label',
                style={
                    'display':'none',
                    'color': '#FF0000'
                }
            ),
            html.Label(
                "Set valid number of clusters, integer >= 2!",
                id='error_no_of_clusters',
                style={
                    'display':'none',
                    'color': '#FF0000'
                }
            ),
            dcc.Dropdown(
                id="laySelection",
                value= 'preset',
                clearable=False,
                options= [
                    {'label': name, 'value': val}
                    for name, val in [['Preset (recommended)', 'preset'], ['Breadthfirst', 'breadthfirst'],
                                    ['Cose', 'cose'], ['Dagre', 'dagre'], ['Spread', 'spread']]
                ],
                style={
                    'marginBottom' : '15px',
                    'marginTop' : '15px',
                    'background-color' : '#F5F5F5'
                }
            ),
            dbc.Button("CREATE VISUALIZATION",
                    id = 'visualize',
                    className = 'btn-primary d-grid gap-2',
                    color="primary",
                    # block=True,
                    style={
                        'marginBottom' : '15px',
                        'marginTop' : '15px',
                    }
            ),
            html.Label(
                "Do clustering first!",
                id='do_clustering_label',
                style={
                    'display':'none',
                    'color': '#FF0000'
                }
            ),
            html.Div(
                style={
                    'borderStyle': 'solid',
                    'display' : 'flex',
                    'border-color' : '#343a40',
                    'border-width' : '1px',
                    'border-radius' : '6px'
                },
                children = [
                    cyto.Cytoscape(
                        id='visualization',
                        stylesheet=my_stylesheet,
                        layout = {'name' : 'breadthfirst'},
                        style= {
                            'width': '80%',
                            'height': '550px',
                            'margin':'auto',
                            'box-sizing': 'border-box',
                            'background-color': '#F5F5F5',
                            'color' : '#F5F5F5'
                        },
                        elements = [ ]

                    ),
                    html.Div(
                        style={
                                'width': '20%',
                                'height': '550px',
                                'padding-top': '10px',
                                'box-sizing': 'border-box',
                                'border-left': 'solid 1px',
                                'padding-left': '10px'
                            },
                        children = [

                            html.Div(
                                id="legend",
                                style={
                                'height': '280px'
                                },
                                children=[]
                            ),
                            html.Div(
                                style={
                                    'height': '260px',
                                    'overflow-y': 'scroll'
                                },
                                children=[
                                    html.H4(id= 'node_label', style={'whiteSpace': 'pre-wrap'}),
                                    html.P(id='node_cluster_info',  style={'whiteSpace': 'pre-wrap'}),
                                    html.P(id='node_text',  style={'whiteSpace': 'pre-wrap'})
                                ]
                            )
                        ]
                    )
                ]
            ),
            dbc.Button("EXPAND GRAPH",
                    id = 'expand',
                    className = 'btn btn-primary blue-gradient waves-effect d-grid gap-2',
                    color = 'primary',
                    # block=True,
                    style={
                        'marginBottom' : '15px',
                        'marginTop' : '15px',
                    }
            ),
            html.Div([
                html.Div([
                    html.H5("Graph Report"),
                    html.P(
                        style={
                            'padding-right' : '15px',
                            'padding-left' : '15px'
                        },
                        id='graph-report-table'
                    ),
                    html.H5("Clustering Report"),
                    html.P(style={
                            'padding-right' : '15px',
                            'padding-left' : '15px'
                    },
                    id='clust-results-table'),
                ]),

        ])
    ]
    )

legendLouvain=[
    html.H4("Legend", style={'whiteSpace': 'pre-wrap'}),
    html.Div(
        style={
            'display':'flex',
            'align-items':'center',
            'text-align':'center',
            'margin-bottom':'10px',
        },
        children=[
            html.Div(
                style={ 
                        'width':'15px',
                        'height':'15px',
                        'border':'solid 1px',
                        'display':'flex',
                        'align-items':'center',
                        'transform':'rotate(45deg)',
                        'margin-left':'2px'     
                },
            ),
            html.P('Main (graph) node',style={
                'whiteSpace': 'pre-wrap',
                'margin':'0 0 0 20px'})
        ]
    ),
    html.Div(
        style={
            'display':'flex',
            'align-items':'center',
            'text-align':'center',
            'margin-bottom':'10px'
        },
        children=[
            html.Div(
                style={ 
                        'width':'15px',
                        'height':'15px',
                        'border':'solid 1px',
                        'display':'flex',
                        'align-items':'center',
                        'transform':'rotate(45deg)',
                        'margin-left':'2px',
                        'background-color':'#009fff'   
                },
            ),
            html.P('Virtual (community) node',style={'whiteSpace': 'pre-wrap','margin':'0 0 0 20px'})
        ]
    ),
    html.Div(
        style={
            'margin-left':'20px',
            'display':'flex',
            'align-items':'center',
            'text-align':'center',
            'margin-bottom':'10px'
        },
        children=[
            html.Div(
                style={ 
                        'width':'15px',
                        'height':'15px',
                        'border':'solid 1px',
                        'display':'flex',
                        'align-items':'center',
                        'transform':'rotate(45deg)',
                        'margin-left':'2px',
                        'overflow':'hidden'    
                },
                children=[
                    html.Img(src=black_star,style={'transform':'rotate(-45deg)','height':'90%'})
                ]
            ),
            html.P('Show important nodes',style={'whiteSpace': 'pre-wrap','margin':'0 0 0 20px'})
        ]
    ),
    html.Div(
        style={
            'margin-left':'20px',
            'display':'flex',
            'align-items':'center',
            'text-align':'center',
            'margin-bottom':'10px'
        },
        children=[
            html.Div(
                style={ 
                        'width':'15px',
                        'height':'15px',
                        'border':'solid 1px',
                        'display':'flex',
                        'align-items':'center',
                        'transform':'rotate(45deg)',
                        'margin-left':'2px'     
                },
                children=[
                    html.Img(src=plusImage,style={'transform':'rotate(-45deg)','height':'100%'})
                ]
            ),
            html.P('Show all child nodes',style={'whiteSpace': 'pre-wrap','margin':'0 0 0 20px'})
        ]
    ),
    html.Div(
        style={
            'margin-left':'20px',
            'display':'flex',
            'align-items':'center',
            'text-align':'center',
            'margin-bottom':'10px'
        },
        children=[
            html.Div(
                style={ 
                        'width':'15px',
                        'height':'15px',
                        'border':'solid 1px',
                        'display':'flex',
                        'align-items':'center',
                        'transform':'rotate(45deg)',
                        'margin-left':'2px'    
                },
                children=[
                    html.Img(src=minusImage,style={'transform':'rotate(-45deg)','height':'2px', 'width':'100%'})
                ]
            ),
            html.P('Collapse all nodes',style={'whiteSpace': 'pre-wrap','margin':'0 0 0 20px'})
        ]
    ),
    
    html.Div(
        style={
            'display':'flex',
            'align-items':'center',
            'text-align':'center',
            'margin-bottom':'10px'
        },
        children=[
            html.Img(src=starImage,
                style={ 'width':'22px'}
            ),
            html.P('Community important node',style={'whiteSpace': 'pre-wrap','margin':'0 0 0 18px'})
        ]
    ),
    html.Div(
        style={
            'display':'flex',
            'align-items':'center',
            'text-align':'center',
            'margin-bottom':'10px'
        },
        children=[
            html.Div(
                style={ 
                    'width':'20px',
                    'height':'20px',
                    'borderRadius':'50%',
                    'background-color':'#009fff'
                    }
            ),
            html.P('Community element node',style={'whiteSpace': 'pre-wrap','margin':'0 0 0 18px'})
        ]
    ),
]

legendAglomerative=[
    html.H4("Legend", style={'whiteSpace': 'pre-wrap'}),
    html.Div(
        style={
            'display':'flex',
            'align-items':'center',
            'text-align':'center',
            'margin-bottom':'10px'
        },
        children=[
            html.Div(
                style={ 
                        'width':'15px',
                        'height':'15px',
                        'border':'solid 1px',
                        'display':'flex',
                        'align-items':'center',
                        'transform':'rotate(45deg)',
                        'margin-left':'2px'     
                },
            ),
            html.P('Cluster connecting node',style={'whiteSpace': 'pre-wrap','margin':'0 0 0 20px'})
        ]
    ),
    html.Div(
        style={
            'margin-left':'20px',
            'display':'flex',
            'align-items':'center',
            'text-align':'center',
            'margin-bottom':'10px'
        },
        children=[
            html.Div(
                style={ 
                        'width':'15px',
                        'height':'15px',
                        'border':'solid 1px',
                        'display':'flex',
                        'align-items':'center',
                        'transform':'rotate(45deg)',
                        'margin-left':'2px'     
                },
                children=[
                    html.Img(src=plusImage,style={'transform':'rotate(-45deg)', 'height':'100%'})
                ]
            ),
            html.P('Expand',style={'whiteSpace': 'pre-wrap','margin':'0 0 0 20px'})
        ]
    ),
    html.Div(
        style={
            'margin-left':'20px',
            'display':'flex',
            'align-items':'center',
            'text-align':'center',
            'margin-bottom':'10px'
        },
        children=[
            html.Div(
                style={ 
                        'width':'15px',
                        'height':'15px',
                        'border':'solid 1px',
                        'display':'flex',
                        'align-items':'center',
                        'transform':'rotate(45deg)',
                        'margin-left':'2px'    
                },
                children=[
                    html.Img(src=minusImage,style={'transform':'rotate(-45deg)', 'height':'2px', 'width':'100%'})
                ]
            ),
            html.P('Collapse',style={'whiteSpace': 'pre-wrap','margin':'0 0 0 20px'})
        ]
    ),
    html.Div(
        style={
            'display':'flex',
            'align-items':'center',
            'text-align':'center',
            'margin-bottom':'10px'
        },
        children=[
            html.Div(
                style={ 
                    'width':'20px',
                    'height':'20px',
                    'borderRadius':'50%',
                    'background-color':'#009fff' ,
                    'display':'flex',
                    'align-items':'center', 
                },
                children=[
                     html.Img(src=plusImage,style={'width':'14px','margin':'auto'}),
                ]
            ),
            html.P('Expand subcluster node',style={'whiteSpace': 'pre-wrap','margin':'0 0 0 20px'})
        ]
    ),
    html.Div(
        style={
            'display':'flex',
            'align-items':'center',
            'text-align':'center',
            'margin-bottom':'10px'
        },
        children=[
            html.Div(
                style={ 
                    'width':'20px',
                    'height':'20px',
                    'borderRadius':'50%',
                    'background-color':'#009fff' ,
                    'display':'flex',
                    'align-items':'center', 
                },
                children=[
                     html.Img(src=minusImage,style={'width':'14px','margin':'auto'}),
                ]
            ),
            html.P('Collapse subcluster node',style={'whiteSpace': 'pre-wrap','margin':'0 0 0 20px'})
        ]
    ),
    html.Div(
        style={
            'display':'flex',
            'align-items':'center',
            'text-align':'center',
            'margin-bottom':'10px'
        },
        children=[
            html.Div(
                style={ 
                    'width':'20px',
                    'height':'20px',
                    'borderRadius':'50%',
                    'background-color':'#009fff'
                    }
            ),
            html.P('Leaf cluster node',style={'whiteSpace': 'pre-wrap','margin':'0 0 0 18px'})
        ]
    ),
]