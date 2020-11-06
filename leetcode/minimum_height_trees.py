# For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

# Format
# The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# Example 1 :

# Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

#         0
#         |
#         1
#        / \
#       2   3 

# Output: [1]
# Example 2 :

# Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

#      0  1  2
#       \ | /
#         3
#         |
#         4
#         |
#         5 

# Output: [3, 4]
# Note:

# According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

# brute force TLE
def findMinHeightTrees(self, n, edges):
        
    maps = collections.defaultdict(list)
    for i in edges:
        maps[i[0]].append(i[1])
        maps[i[1]].append(i[0])
        
    min_val = float('inf')
    mins = []
    target = set(range(n))
    
    for t in range(n):
        temp = set([t])
        stack = set([t])
        height = 0
        
        while temp != target:
            cur = []
            for m in stack:
                cur += [i for i in maps[m] if i not in temp]
            temp.update(set(cur))
            stack = set(cur)
            height += 1
            
        if height < min_val:
            min_val = height
            mins = [t]
        elif height == min_val:
            mins.append(t)
            
    return mins

def findMinHeightTrees(self, n, edges):
    if n == 1: return [0] 
    maps = collections.defaultdict(set)
    
    for i in edges:
        maps[i[0]].add(i[1])
        maps[i[1]].add(i[0])
    
    leaves = set([i for i in maps if len(maps[i]) == 1])
    
    while n > 2:
        n -= len(leaves)
        new_leaves = set()
        for t in leaves:
            i = maps.pop(t)
            maps[list(i)[0]].remove(t)
            
            if len(maps[list(i)[0]]) == 1:
                new_leaves.add(list(i)[0])
        leaves = new_leaves
    
    return list(leaves)

# topological sort
def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    graph = collections.defaultdict(list)
    degree = collections.Counter()
    
    for i, v in edges:
        graph[i].append(v)
        graph[v].append(i)
        degree[i] += 1
        degree[v] += 1
    
    min_height_nodes = []
    max_val = -float('inf')
    visited = set()
    
    queue = collections.deque([(i, 0) for i in range(n) if degree[i] <= 1])
    while queue:
        node, h = queue.popleft()
        visited.add(node)
        
        if h > max_val:
            min_height_nodes = [node]
            max_val = h
        elif h == max_val:
            min_height_nodes.append(node)
        
        for sub_sequent_node in graph[node]:
            degree[sub_sequent_node] -= 1
            if sub_sequent_node not in visited and degree[sub_sequent_node] == 1:
                visited.add(sub_sequent_node)
                queue.append((sub_sequent_node, h + 1))
    
    return min_height_nodes