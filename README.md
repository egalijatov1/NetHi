# NetHi
An Interactive Web Application for Visualization of Network Clustering and Hierarchical Data 

# Motivation
- Graphs are powerful tools for representation of hierarchies and relations in data
- Graph clustering and representation techniques are attractive fields for decades, even more so, the large networks and hierarchies challenge remains 
- Graphs help us better understand data of almost any kind, since all real-world domain data contains some sort of connections and orders within

# Problems
Networks:
- Networks often have millions of nodes 
- Hard to visualize
- User can be interested only in “important” parts of the network

Hierarchies:
- Usually represented using a dendogram
- All leaf nodes are shown
- User can have better overview when only one part of hierarchy can be shown

# Solution description
NetHi is a web application implemented using Dash (https://dash.plotly.com)
There are three parts of the application:
1. Setup (uploading dataset, selecting algorithm, selecting attributes and clustering)
2. Visualization (selecting layout, navigating through the data)
3. Report (clustering report, graph report)

# Methods
NETWORKS
▪ [Louvain community detection](https://python-louvain.readthedocs.io/en/latest/api.html)
▪ [Spring layout coordinates computation and translation](https://networkx.github.io/documentation/networkx-1.9/reference/generated/networkx.drawing.layout.spring_layout.html)
▪ Graph construction (community nodes, virtual community nodes connected to all community nodes)

HIERARCHIES
▪ [Agglomerative clustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html)
▪ Creating hierarchical structure
▪ Graph construction (adding sub-cluster nodes and connecting them to the leaf nodes)

VISUALIZATION
▪ [Dash Cytoscape](https://dash.plotly.com/cytoscape)
▪ Coloring with [matplotlib.cm5](https://matplotlib.org/api/cm_api.html)
▪ Expanding and collapsing
▪ Node information presentation on hover

# Architecture
Architecture of the solution resembles MVC architecture in a following way:
![image](https://user-images.githubusercontent.com/88715320/155353691-458fccfd-1f4f-44d8-a2a8-4f656bd3dfe8.png)

