# An undirected, connected tree with N nodes labelled 0...N-1 and N-1 edges are given.

# The ith edge connects nodes edges[i][0] and edges[i][1] together.

# Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.

# Example 1:

# Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# Output: [8,12,6,10,10,10]
# Explanation: 
# Here is a diagram of the given tree:
#   0
#  / \
# 1   2
#    /|\
#   3 4 5
# We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.

import collections

def sumOfDistancesInTree(N, edges):
        
    d = collections.defaultdict(list)
    
    for i in edges:
        d[i[0]].append(i[1])
        d[i[1]].append(i[0])
        
    res = [0] * N
    nodes = [0] * N
    from_point = 0

    def explore(root, level, parent = None):

        current_sum, num_nodes = level, 1

        for i in d[root]:
            if i == parent: continue
            t1, t2 = explore(i, level + 1, root)

            current_sum += t1
            num_nodes += t2
        
        nodes[root] = num_nodes - 1
        return current_sum, num_nodes

    res[0] = explore(0, 0)[0]
    stack = [(i, 0) for i in d[0]]

    while stack:
        n, parent = stack.pop()
        res[n] = res[parent] + N - 2 * nodes[n] - 2
    
        stack += [(i, n) for i in d[n] if i != parent]
    
    return res