# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 15:34:02 2020

@author: DELL
"""

import networkx as nx
G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,1)
print(G.nodes())