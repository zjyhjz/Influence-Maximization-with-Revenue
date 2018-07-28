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

def newGreedyICRev (G, k, I, pi,pa, p=.05, R = 20):
    import random
    S = []
    for i in range(k):
        print(i)
        time2k = time.time()
        scores = {v: 0 for v in G}
        for j in range(R):
            E = deepcopy(G)
            edge_rem = [e for e in E.edges() if random.random() < (1 - p) ** (E[e[0]][e[1]]['weight'])]
            E.remove_edges_from(edge_rem)
            As,Is = bfs(E,S,I)
            cnt1 = {}
            cnt2 = {}
            for v in G:
                cnt1[v],cnt2[v] = bfs(E,{v},I)
            for v in G:
                if v not in S:
                    if v not in As:
                        if v not in Is:
                            scores[v] += float(len(cnt1[v])+pi/pa*len(cnt2[v]))/R

        max_v, max_score = max(scores.items(), key = lambda scores: scores[1])
        S.append(max_v)
        print ('')
        print(time.time() - time2k)
    return S