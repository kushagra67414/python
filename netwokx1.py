# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 17:04:21 2020

@author: DELL
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.gnp_random_graph(50,0.3)
nx.draw(G)
plt.show()

nx.write_gexf(G, "analyse.txt")