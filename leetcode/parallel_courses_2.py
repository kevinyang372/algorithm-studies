# Given the integer n representing the number of courses at some university labeled from 1 to n, and the array dependencies where dependencies[i] = [xi, yi]  represents a prerequisite relationship, that is, the course xi must be taken before the course yi.  Also, you are given the integer k.

# In one semester you can take at most k courses as long as you have taken all the prerequisites for the courses you are taking.

# Return the minimum number of semesters to take all courses. It is guaranteed that you can take all courses in some way.

 

# Example 1:



# Input: n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
# Output: 3 
# Explanation: The figure above represents the given graph. In this case we can take courses 2 and 3 in the first semester, then take course 1 in the second semester and finally take course 4 in the third semester.
# Example 2:



# Input: n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
# Output: 4 
# Explanation: The figure above represents the given graph. In this case one optimal way to take all courses is: take courses 2 and 3 in the first semester and take course 4 in the second semester, then take course 1 in the third semester and finally take course 5 in the fourth semester.
# Example 3:

# Input: n = 11, dependencies = [], k = 2
# Output: 6
 

# Constraints:

# 1 <= n <= 15
# 1 <= k <= n
# 0 <= dependencies.length <= n * (n-1) / 2
# dependencies[i].length == 2
# 1 <= xi, yi <= n
# xi != yi
# All prerequisite relationships are distinct, that is, dependencies[i] != dependencies[j].
# The given graph is a directed acyclic graph.

from itertools import combinations
import math

def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
    graph = collections.defaultdict(list)
    indegree = collections.Counter()
    
    for n1, n2 in dependencies:
        indegree[n2] += 1
        graph[n1].append(n2)
        
    for node in range(1, n + 1):
        if node not in indegree:
            indegree[node] = 0
    
    def hash_d(d):
        return ",".join(":".join([str(key), str(val)]) for key, val in d.items())
    
    def unhash_d(s):
        if not s: return {}
        return {int(n.split(":")[0]):int(n.split(":")[1]) for n in s.split(",")}
    
    @lru_cache
    def search(s, num_semesters):
        ind = unhash_d(s)
        queue = set([node for node, count in ind.items() if count == 0])
        
        if not ind: return num_semesters
        if len(queue) == len(ind): return math.ceil(len(queue) / k) + num_semesters
        
        if len(queue) <= k:
            for node in queue:
                del ind[node]
                for child in graph[node]:
                    ind[child] -= 1
            
            return search(hash_d(ind), num_semesters + 1)
        else:
            possible_queues = combinations(queue, k)
            min_val = float('inf')
            
            for q in possible_queues:
                c_ind = dict(ind)
                for node in q:
                    del c_ind[node]
                    for child in graph[node]:
                        c_ind[child] -= 1
                min_val = min(search(hash_d(c_ind), num_semesters + 1), min_val)
            
            return min_val
                 
    return search(hash_d(indegree), 0)