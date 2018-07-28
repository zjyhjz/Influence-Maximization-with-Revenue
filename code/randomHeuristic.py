def randomHeuristic(G, k, p=.01):
    ''' Finds initial set of nodes to propagate in Independent Cascade model
    Input: G -- networkx graph object
    k -- number of nodes needed
    p -- propagation probability
    Output:
    S -- chosen k nodes
    '''
    import random
    S = random.sample(G.nodes(), k)
    return S