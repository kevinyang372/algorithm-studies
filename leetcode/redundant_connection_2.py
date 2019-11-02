# In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

# The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.

# Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

# Example 1:
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given directed graph will be like this:
#   1
#  / \
# v   v
# 2-->3
# Example 2:
# Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# Output: [4,1]
# Explanation: The given directed graph will be like this:
# 5 <- 1 -> 2
#      ^    |
#      |    v
#      4 <- 3
# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.

class DSU:
    def __init__(self):
        self.d = [i for i in range(1001)]
        
    def find(self, val):
        if self.d[val] != val:
            self.d[val] = self.find(self.d[val])
        return self.d[val]
    
    def union(self, x, y):
        self.d[self.find(x)] = self.d[y]

class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        
        def circleDetection(graph, start, c1, c2):
            for candidate in [c1, c2]:
                m = candidate
                while graph[candidate]:
                    if graph[candidate][0] == start:
                        return [m, start]
                    else:
                        candidate = graph[candidate][0]
            return [c2, start]
        
        dsu = DSU()
        indegree = collections.defaultdict(list)
        over = None
        
        for x, y in edges:
            indegree[y].append(x)
            if len(indegree[y]) > 1:
                over = y
                
        if over:
            return circleDetection(indegree, over, indegree[over][0], indegree[over][1])
            
        for x, y in edges:
            if dsu.find(y) == dsu.find(x):
                return [x, y]
            indegree[y].append(x)
            dsu.union(x, y)
        
        for i in indegree:
            if indegree[i] > 1:
                for x in indegree[i]:
                    if len(indegree[x]) < 1:
                        return [x, i]
        return None