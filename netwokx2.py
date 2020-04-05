# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 12:06:32 2020

@author: DELL
"""

import networkx as nx
import numpy 
G = nx.read_edgelist("facebook_combined.txt")
N= list(G.node())
spll = []
for v in N:
    for u in N:
        if u!=v:
            l = nx.shortest_path_length(G,u,v)
            print("shortest path link" , u , "and" ,v , "is of lenght" ,l )
            spll.append(l)
            
min_spl= min(spll)
max_spl = max(spll) 

avg_apl = numpy.average(spll)

print("minimun shortest path length:",min_spl)
print("maximun shortest path length:",max_spl)
print("averGE shortest path length:",avg_apl)

