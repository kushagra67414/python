# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:27:24 2020

@author: DELL
"""

import networkx as nx
import random
import matplotlib.pyplot as plt
def add_edges():
    node=list(G.nodes())
    
    for s in node:
        for r in node:
            if s!=r:
                r=random.random()
                if r<=0.5:
                    G.add_edge(s,r)
                    
    return G
def  assign_points(G):
    nodes=list(G.nodes)
    p = []
    for each in nodes:
        p.append(100)
        
    return p


        
def keep_distributing(points,G):
    while(1):
        new_points=distribute_points(G,points)
        print(new_points)
                                      
        stop = input("press # to stop")
        if stop =='#' :
            break
    return new_points
def  distribute_points(G,points):
    nodes= list(G.nodes())
    new_points=[]
    for i in range(len(nodes)):
        new_points.append(0)
        
    for n in nodes:
        out = list(G.out_edges())
        if(len(out)==0):
            new_points[n] = new_points[n]   + points[n]
        else:
            share= points[n]/ len(out)
            for (src,tgt) in out :
                new_points[tgt]=new_points[tgt] + share
                
    return new_points   
     
G= nx.DiGraph()
G.add_nodes_from([i for i in range(5)])
G = add_edges()

nx.draw(G,with_labels=True)
plt.show()

points= assign_points(G)
final_points= keep_distributing(points,G)





