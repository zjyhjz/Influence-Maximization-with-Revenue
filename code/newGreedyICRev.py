from __future__ import division
from copy import deepcopy # copy graph object
from random import random
from priorityQueue import PriorityQueue as PQ
import networkx as nx
from runIAC import avgIAC
import time


def bfs(E, S):
    ''' Finds all vertices reachable from subset S in graph E using Breadth-First Search
    Input: E -- networkx graph object
    S -- list of initial vertices
    Output: Rs -- list of vertices reachable from S
    '''
    Rs = []
    for u in S:
        if u in E:
            if u not in Rs: Rs.append(u)
            for v in E[u]:
                if v not in Rs: Rs.append(v)
    return Rs

def findCCs(G, p):
    # remove blocked edges from graph G
    import random
    E = deepcopy(G)
    edge_rem = [e for e in E.edges() if random.random() < (1-p)**(E[e[0]][e[1]]['weight'])]
    E.remove_edges_from(edge_rem)

    # initialize CC
    CCs = dict() # each component is reflection of the number of a component to its members

    return CCs
'''    explored = dict(zip(E.nodes(), [False]*len(E)))
    c = 0
    # perform BFS to discover CC
    for node in E:
        if not explored[node]:
            c += 1
            explored[node] = True
            CCs[c] = [node]
            component = E[node].keys()
            for neighbor in component:
                if not explored[neighbor]:
                    explored[neighbor] = True
                    CCs[c].append(neighbor)
                    component.extend(E[neighbor].keys())'''


def newGreedyIC (G, k, p=.05, R = 20):
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
            Rs = bfs(E,S)
            cnt = {}
            for v in G:
                cnt[v] = bfs(E,{v})
            for v in G:
                if v not in S:
                    if v not in Rs:
                        scores[v] += float(len(cnt[v]))/R

        max_v, max_score = max(scores.items(), key = lambda scores: scores[1])
        S.append(max_v)
        print ('')
        print(time.time() - time2k)
    return S

