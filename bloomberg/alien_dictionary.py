# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

# Example 1:

# Input:
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]

# Output: "wertf"
# Example 2:

# Input:
# [
#   "z",
#   "x"
# ]

# Output: "zx"
# Example 3:

# Input:
# [
#   "z",
#   "x",
#   "z"
# ] 

# Output: "" 

# Explanation: The order is invalid, so return "".
# Note:

# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.

# topological sort
def alienOrder(self, words):
        
    graph = {}
    for i in words:
        for c in i:
            graph[c] = set()
            
    for i in range(len(words) - 1):
        for j in range(min(len(words[i]), len(words[i + 1]))):
            if words[i][j] != words[i + 1][j]:
                graph[words[i][j]].add(words[i + 1][j])
                break
    
    def topologicalsort(graph):
        degree = collections.defaultdict(int)
        
        for node in graph:
            for neighbor in graph[node]:
                degree[neighbor] += 1
                
        order = ''
        queue = [node for node in graph if degree[node] == 0]
        heapq.heapify(queue)
        
        while queue:
            node = heapq.heappop(queue)
            order += node
            
            for neighbor in graph[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    heapq.heappush(queue, neighbor)
        
        if len(order) == len(graph):
            return order
        else:
            return ''
            
    return topologicalsort(graph)

