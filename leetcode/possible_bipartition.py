# Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

# Each person may dislike some other people, and they should not go into the same group. 

# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

# Return true if and only if it is possible to split everyone into two groups in this way.

 

# Example 1:

# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]
# Example 2:

# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
# Example 3:

# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false
 

# Note:

# 1 <= N <= 2000
# 0 <= dislikes.length <= 10000
# 1 <= dislikes[i][j] <= N
# dislikes[i][0] < dislikes[i][1]
# There does not exist i != j for which dislikes[i] == dislikes[j].

def possibleBipartition(self, N, dislikes):
        
    graph = collections.defaultdict(set)
    
    for i, j in dislikes:
        graph[i].add(j)
        graph[j].add(i)
        
    d = [set(), set()]
    visited = set()
    
    def dfs(node, ind):
        if node in d[1 - ind]: return False
        if node in visited: return True
        
        visited.add(node)
        d[ind].add(node)
        
        for k in graph[node]:
            temp = dfs(k, 1 - ind)
            if not temp: return False
        
        return True
        
    for i in range(1, N + 1):
        if i in visited: continue
        temp = dfs(i, 0)
        if not temp: return False
        
    return True

# dfs
def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
    graph = collections.defaultdict(set)
    
    for x, y in dislikes:
        graph[x].add(y)
        graph[y].add(x)
        
    visited = [-1] * (N + 1)
    def dfs(node, curr_level):
        if visited[node] > -1: return (curr_level - visited[node]) % 2 == 0
        
        visited[node] = curr_level
        for next in graph[node]:
            if not dfs(next, curr_level + 1): 
                return False
        return True
    
    for n in range(1, N + 1):
        if visited[n] < 0 and not dfs(n, 0): 
            print(n)
            return False
    
    return True