''' File for testing different files
'''

import networkx as nx
import random

from IC import runIC
from degreeDiscount import degreeDiscountIC
from randomHeuristic import randomHeuristic
from degreeHeuristic import degreeHeuristic
from newGreedyICRev import newGreedyIC
from newGreedyRevMine import newGreedyICRev
from RDGA import Rev
#import matplotlib.pylab as plt
import os

if __name__ == '__main__':
    import time
    start = time.clock()

    # read in graph
    G = nx.Graph()
    with open('graphdata/hep.txt') as f:
        n, m = f.readline().split()
        I = [([0] * int(m)) for i in range(int(n))]
        for line in f:
            u, v = map(int, line.split())
            if random.random() < 0.25:
                I[u][v] = 1
            try:
                G[u][v]['weight'] += 1
            except:
                G.add_edge(u,v, weight=1)
            # G.add_edge(u, v, weight=1)
    print('Built graph G')

    #calculate initial set
    seed_size = 50 #initial number of seed nodes
    pi = 0.5 #payoff of one informed node
    pa = 1 #payoff of one active node
    #change the function to simulate different methods
    #S = randomHeuristic(G, seed_size, p=.05)
    #S = degreeDiscountIC(G, seed_size, p=.05)
    #S = degreeHeuristic(G,seed_size,p=.05)
    #S = newGreedyIC(G, seed_size, p=.05)
    #S = newGreedyICRev(G, seed_size, I, pi, pa, p=.05)

    #print('Initial set of', seed_size, 'nodes chosen')

    start = time.clock()
    c1 = 0.8 #seed node cost=0.8
    S= Rev(G, seed_size, I, pi, pa, c1)
    #S = randomHeuristic(G, seed_size, p=.05)
    #S = newGreedyICRev(G, seed_size, I, pi, pa, p=.05)
    #S = newGreedyIC(G, seed_size, p=.05)
    time1 = time.clock() - start
    iterations = 200  # number of iterations
    avg1 = 0
    avg2 = 0
    for i in range(iterations):
        T, In = runIC(G, S, I)
        avg1 += float(len(T)) / iterations
        avg2 += float(len(In)) / iterations
    pr_res = str(seed_size)
    l1 = len(S)
    rev1 = int(round(avg1)) + pi * int(round(avg2)) -  c1 * l1

    c2 = 1.2 #seed node cost=1.2

    S = degreeDiscountIC(G, seed_size, p=.05)
    #S = Rev(G, seed_size, I, pi, pa, c2)
    avg1 = 0
    avg2 = 0
    for i in range(iterations):
        T, In = runIC(G, S, I)
        avg1 += float(len(T)) / iterations
        avg2 += float(len(In)) / iterations
    l2 = len(S)
    rev2 = int(round(avg1)) + pi * int(round(avg2)) - c2 * l2
    pr_res += '\t' + str(round(rev1,3)) + '\t' + str(round(rev2,3)) + '\t' + str(l1) + '\t' + str(l2)+ '\t' + str(time1) + '\n'

    print(pr_res)
