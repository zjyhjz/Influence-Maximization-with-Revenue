from __future__ import division
from copy import deepcopy # copy graph object
from random import random
from priorityQueue import PriorityQueue as PQ
import networkx as nx
from runIAC import avgIAC
import time


def bfs(E, S ,I):
    ''' Finds all vertices reachable from subset S in graph E using Breadth-First Search
    Input: E -- networkx graph object
    S -- list of initial vertices
    Output: Rs -- list of vertices reachable from S
    '''
    As = []
    Is = []
    for u in S:
        if u in E:
            if u not in As: As.append(u)
            for v in E[u]:
                if I[u][v] == 0:
                    if v in Is:
                        Is.remove(v)
                    if v not in As:
                        As.append(v)
                else:
                    if v not in Is:Is.append(v)
    return As,Is

def r(E,S,I,pi,pa,c,k):
    A,In = bfs(E,S,I)
    rev = pa * len(A) + pi * len(In) - c * k
    return rev

def Rev (G, k, I, pi,pa,c):
    import random
    S = []
    S1 = []
    S2 = []
    flag = {}
    de = {}
    max_r = 0
    for v in G:
        de[v] = r(G,{v},I,pi,pa,c,1)
        flag[v] = 0
    while len(S1) < k :
        v, dl = max(de.items(),key=lambda d:d[1])
        if flag[v] == len(S1):
            S1.append(v)
            tmp = r(G, S1, I, pi, pa, c, len(S1))
            if tmp > max_r:
                S = S1.copy()
                max_r = tmp
        else:
            S2 = S1.copy()
            S2.append(v)
            de[v] = r(G,S2,I,pi,pa,c,len(S2)) - r(G,S1,I,pi,pa,c,len(S1))
            flag[v] = len(S1)
    return S1
