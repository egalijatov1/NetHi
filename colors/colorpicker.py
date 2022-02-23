
from random import randint
import matplotlib.cm as cm
import numpy as np
from matplotlib.colors import rgb2hex
import matplotlib.pyplot as plt


def view_colormap(cmap):
    """Plot a colormap with its grayscale equivalent"""
    colors = cmap
    
    fig, ax = plt.subplots(2, figsize=(6, 2),
                           subplot_kw=dict(xticks=[], yticks=[]))
    ax[0].imshow([colors], extent=[0, 10, 0, 1])
    plt.show()
f  = open("gist_rainbowtest-100colors.txt", "w+")

#set colormap and create list of different shuffled colors used for clusters
colors = cm.gist_rainbow(np.linspace(0, 1, 100))
colors=colors[:,:3]
colors=np.array(colors)
np.random.shuffle(colors)
B = np.array(colors*255, dtype=int) # convert to int

# Define a function for the mapping
rgb2hex = lambda r,g,b: '#%02x%02x%02x' %(r,g,b)

colors_write=[ rgb2hex(*B[i,:]) for i in range(B.shape[0]) ]

"""
Simple distinct colors for first 18 clusters
colors_write=['#42d4f4','#911eb4','#f58231','#4363d8','#ffe119','#3cb44b','#e6194B','#bfef45','#000075','#fabed4',
'#800000','#f032e6','#aaffc3','#ffd8b1','#dcbeff','#469990','#fffac8','#808000']
"""

#writing to folder colors as css classes for both clusters and lines of clusters
for i in range(len(colors_write)):
    f.write("{\r\t'selector': '.%d',\r\t'style':{\r\t\t'background-color':'%s'\r\t}\r},\r"%(i,colors_write[i]))

for i in range(len(colors_write)):
    f.write("{\r\t'selector': '.%de',\r\t'style':{\r\t\t'line-color':'%s',\r\t\t'width':1\r\t}\r},\r"%(i,colors_write[i]))
f.close() 



#view_colormap(colors)

