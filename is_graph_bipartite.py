# Given an undirected graph, return true if and only if it is bipartite.

# Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

# The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

# Example 1:
# Input: [[1,3], [0,2], [1,3], [0,2]]
# Output: true
# Explanation: 
# The graph looks like this:
# 0----1
# |    |
# |    |
# 3----2
# We can divide the vertices into two groups: {0, 2} and {1, 3}.
# Example 2:
# Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
# Output: false
# Explanation: 
# The graph looks like this:
# 0----1
# | \  |
# |  \ |
# 3----2
# We cannot find a way to divide the set of nodes into two independent subsets.
 

# Note:

# graph will have length in range [1, 100].
# graph[i] will contain integers in range [0, graph.length - 1].
# graph[i] will not contain i or duplicate values.
# The graph is undirected: if any element j is in graph[i], then i will be in graph[j].

#dfs
def isBipartite(self, graph):
        
    not_seen = set([i for i in range(len(graph))])
    
    while len(not_seen) > 0:
        d = {list(not_seen)[0]:0}
        stack = [list(not_seen)[0]]

        while stack:
            node = stack.pop()
            if node not in not_seen: continue

            not_seen.remove(node)
            edges = graph[node]
            group = 1 - d[node]

            for i in edges:
                if i in d and d[i] != group: return False
                d[i] = group

            stack += edges
    
    return True