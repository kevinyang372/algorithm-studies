# There are a total of n courses you have to take, labeled from 0 to n-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# Example 1:

# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
# Note:

# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.

import collections

def canFinish(numCourses, prerequisites):

    require = collections.defaultdict(set)

    for i in prerequisites:
        require[i[0]].add(i[1])

    stack = [i for i in range(numCourses) if i not in require]
    
    while stack:
        res = []
        for course in stack:
            for t in require:
                if course in require[t]:
                    require[t].remove(course)
                    if not require[t]:
                        res.append(t)
                        
        for i in res:
            require.pop(i)
            
        stack = res
            
        if not res and require:
            return False
        elif not require:
            return True
