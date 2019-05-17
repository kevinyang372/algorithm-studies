# There are a total of n courses you have to take, labeled from 0 to n-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

# Example 1:

# Input: 2, [[1,0]] 
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
#              course 0. So the correct course order is [0,1] .
# Example 2:

# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
#              courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
#              So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
# Note:

# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.

def findOrder(numCourses, prerequisites):

    if len(prerequisites) == 0:
        return [i for i in range(numCourses)]

    graph = {}
    root = []

    for i in prerequisites:

        if i[0] in graph.keys():
            sub = graph[i[0]]
        else:
            sub = course_nodes(i[0])
            graph[i[0]] = sub

        if i[1] in graph.keys():
            pre = graph[i[1]]
        else:
            pre = course_nodes(i[1])
            graph[i[1]] = pre

        if sub in pre.pre:
            return []

        sub.pre.append(pre)
        pre.sub.append(sub)

        if len(root) == 0 or sub not in root:
            root.append(pre)
        else:
            root[root.index(sub)] = pre

    course_order = []
    waiting_list = root

    while len(course_order) < numCourses and len(waiting_list) != 0:
        current_node = waiting_list.pop(0)

        if current_node.node in course_order or not set([i.node for i in current_node.pre]).issubset(set(course_order)):
            continue

        course_order.append(current_node.node)
        waiting_list += current_node.sub

    if len(course_order) < numCourses:
        all_course = [i for i in range(numCourses)]
        course_order += list(all_course - graph.keys())

        if len(course_order) < numCourses:
            return []

    return course_order


class course_nodes:

    def __init__(self, value):
        self.node = value
        self.pre = []
        self.sub = []