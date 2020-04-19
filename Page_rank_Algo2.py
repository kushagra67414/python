# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 16:28:50 2020

@author: DELL
"""

import networkx as nx
import matplotlib.pyplot as plt
G= nx.read_edgelist(r"C:\Users\DELL\Desktop\Python_code\page_rank_edges.txt", create_using= nx.DiGraph(), nodetype= int)
nx.draw(G,with_labels=True)
plt.show()
