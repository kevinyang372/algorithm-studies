# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

# Note:

# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# Example 1:

# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# Example 2:

# Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
#              But it is larger in lexical order.

# dfs
def findItinerary(self, tickets):
    d = collections.defaultdict(list)
    head = 'JFK'
    
    for i in tickets:
        d[i[0]].append(i[1])
    
    def dfs(node, check):
        if not check: return [node]
        if node not in check: return False
        
        for i in sorted(check[node]):
            check[node].remove(i)
            if not check[node]:
                check.pop(node)
                
            res = dfs(i, check)
            if res != False: 
                return [node] + res
            check[node].append(i)
        return False
    
    return dfs(head, d)