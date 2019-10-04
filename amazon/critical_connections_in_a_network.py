# There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

# A critical connection is a connection that, if removed, will make some server unable to reach some other server.

# Return all critical connections in the network in any order.

 

# Example 1:



# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.
 

# Constraints:

# 1 <= n <= 10^5
# n-1 <= connections.length <= 10^5
# connections[i][0] != connections[i][1]
# There are no repeated connections.

# tarjan algorithm
def criticalConnections(self, n, connections):
        
    graph = collections.defaultdict(list)
    
    for x, y in connections:
        graph[x].append(y)
        graph[y].append(x)
        
    self.cur = 0
    dfn = [None for _ in range(n)]
    low = [None for _ in range(n)]
    
    def dfs(node, parent):
        if dfn[node] is None:
            dfn[node] = self.cur
            low[node] = self.cur
            self.cur += 1
            
            for i in graph[node]:
                if dfn[i] is None:
                    dfs(i, node)
            
            if parent is not None:
                low[node] = min([low[t] for t in graph[node] if t != parent] + [low[node]])
    
    dfs(0, None)
    
    res = []
    for x, y in connections:
        if low[x] > dfn[y] or low[y] > dfn[x]:
            res.append((x, y))
    return res