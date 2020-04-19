# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 20:59:34 2020

@author: DELL
"""

import networkx as nx
import random
import matplotlib.pyplot as plt

g= nx.gnp_random_graph(10,0.5,directed=True)
nx.draw(g,with_labels=True)
x= random.choice([i for i in range(g.number_of_nodes())])
dict_count= {}
for i in range(g.number_of_nodes()):
    dict_count[i]=0

dict_count[x]= dict_count[x] +1
for i in range(100000):
    list_n = list(g.neighbors(x))
    if(len (list_n)==0):
        
        x=random.choice([i for i in range(g.number_of_nodes())])
        dict_count[x]= dict_count[x] +1
    else:
        x=random.choice(list_n)
        dict_count[x]= dict_count[x] +1
        
p=nx.pagerank(g)
print(p)
print(dict_count)