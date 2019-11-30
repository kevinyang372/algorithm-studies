# A tree rooted at node 0 is given as follows:

# The number of nodes is nodes;
# The value of the i-th node is value[i];
# The parent of the i-th node is parent[i].
# Remove every subtree whose sum of values of nodes is zero.

# After doing so, return the number of nodes remaining in the tree.

 

# Example 1:



# Input: nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]
# Output: 2
 

# Constraints:

# 1 <= nodes <= 10^4
# -10^5 <= value[i] <= 10^5
# parent.length == nodes
# parent[0] == -1 which indicates that 0 is the root.

def deleteTreeNodes(self, nodes, parent, value):
        
    graph = collections.defaultdict(list)
    for i, v in enumerate(parent):
        if v != -1:
            graph[v].append(i)
    
    def traverse(node):
        if not graph[node]:
            if value[node] == 0:
                return value[node], -1, 1
            else:
                return value[node], 0, 1
        
        curr, minus, total = value[node], 0, 1
        for m in graph[node]:
            t1, t2, t3 = traverse(m)
            curr += t1
            minus += t2
            total += t3
            
        if curr == 0:
            minus = -total
        return curr, minus, total
    
    _, t1, t2 = traverse(0)
    return t2 + t1