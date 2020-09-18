# Alice and Bob have an undirected graph of n nodes and 3 types of edges:

# Type 1: Can be traversed by Alice only.
# Type 2: Can be traversed by Bob only.
# Type 3: Can by traversed by both Alice and Bob.
# Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

# Return the maximum number of edges you can remove, or return -1 if it's impossible for the graph to be fully traversed by Alice and Bob.

 

# Example 1:



# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
# Output: 2
# Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
# Example 2:



# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
# Output: 0
# Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
# Example 3:



# Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
# Output: -1
# Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.
 

 

# Constraints:

# 1 <= n <= 10^5
# 1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)
# edges[i].length == 3
# 1 <= edges[i][0] <= 3
# 1 <= edges[i][1] < edges[i][2] <= n
# All tuples (typei, ui, vi) are distinct.

def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
    d_alice = {i: i for i in range(1, n + 1)}
    d_bob = {i: i for i in range(1, n + 1)}
    
    def find(d, ind):
        if d[ind] != ind:
            d[ind] = find(d, d[ind])
        return d[ind]
    
    def union(d, i1, i2):
        d[find(d, i1)] = find(d, i2)
    
    edges.sort(reverse=True)
    res = 0
    
    for typ, i, j in edges:
        if typ == 3:
            if find(d_alice, i) == find(d_alice, j) and find(d_bob, i) == find(d_bob, j):
                res += 1
                continue
            union(d_alice, i, j)
            union(d_bob, i, j)
        elif typ == 2:
            if find(d_alice, i) == find(d_alice, j):
                res += 1
                continue
            union(d_alice, i, j)
        else:
            if find(d_bob, i) == find(d_bob, j):
                res += 1
                continue
            union(d_bob, i, j)
            
    for i in range(2, n + 1):
        if find(d_alice, i) != find(d_alice, i-1) or find(d_bob, i) != find(d_bob, i-1):
            return -1
    
    return res