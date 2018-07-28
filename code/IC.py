''' Independent cascade model for influence propagation
'''

def runIC (G, S,I, p = .01):
    ''' Runs independent cascade model.
    Input: G -- networkx graph object
    S -- initial set of vertices
    p -- propagation probability
    Output: T -- resulted influenced set of vertices (including S)
    '''
    from copy import deepcopy
    from random import random
    T = deepcopy(S) # copy already selected nodes
    In = [] #informed node set

    i = 0
    while i < len(T):
        for v in G[T[i]]: # for neighbors of a selected node
            if v not in T and v not in In: # if it wasn't selected yet
                w = G[T[i]][v]['weight'] # count the number of edges between two nodes
                if random() <= 1 - (1-p)**w: # if at least one of edges propagate influence
                    #print(T[i], 'influences', v)
                    if I[T[i]][v] != 1:
                        T.append(v)
                    else:
                        In.append(v)
        i += 1

    return T,In
    
def avgSize(G,S,I,p,iterations):
    avg1 = 0
    avg2 = 0
    for i in range(iterations):
        a,b = runIC(G,S,I,p)
        avg1 += float(len(a))/iterations
        avg2 += float(len(b)) / iterations
    return avg1,avg2
