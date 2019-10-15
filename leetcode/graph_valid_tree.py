# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

# Example 1:

# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true
# Example 2:

# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false
# Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.

def validTree(self, n, edges):
        
    to_visit = set(range(n))
    d = collections.defaultdict(list)
    
    for x, y in edges:
        d[x].append(y)
        d[y].append(x)
    
    queue = collections.deque([0])
    
    while queue:
        node = queue.popleft()
        to_visit.remove(node)
        
        for i in d[node]:
            if i not in to_visit or i in queue:
                return False
            else:
                d[i].remove(node)
                queue.append(i)
        
    return len(to_visit) == 0