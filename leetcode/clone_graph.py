# Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

 

# Example:



# Input:
# {"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

# Explanation:
# Node 1's value is 1, and it has two neighbors: Node 2 and 4.
# Node 2's value is 2, and it has two neighbors: Node 1 and 3.
# Node 3's value is 3, and it has two neighbors: Node 2 and 4.
# Node 4's value is 4, and it has two neighbors: Node 1 and 3.
 

# Note:

# The number of nodes will be between 1 and 100.
# The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
# Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
# You must return the copy of the given node as a reference to the cloned graph.

# hash map + dfs
def cloneGraph(node):
    d = {}
    stack = [node]
    
    while stack:
        n = stack.pop()
        
        if n.val not in d:
            d[n.val] = Node(n.val, [])
        
        for i in n.neighbors:
            if i.val in d:
                if d[i.val] not in d[n.val].neighbors:
                    d[n.val].neighbors.append(d[i.val])
            else:
                d[i.val] = Node(i.val, [])
                d[n.val].neighbors.append(d[i.val])
                stack.append(i)
    
    return d[node.val]


# recursive
def cloneGraph(self, node: 'Node') -> 'Node':
    if not node: return
    
    d = {}
    
    def search(node):
        if node.val in d: return d[node.val]
        
        clone = Node(node.val)
        d[node.val] = clone
        
        for neighbor in node.neighbors:
            clone.neighbors.append(search(neighbor))
        
        return clone
    
    return search(node)