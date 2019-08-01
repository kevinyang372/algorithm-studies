# You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:

# 0 represents the obstacle can't be reached.
# 1 represents the ground can be walked through.
# The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.
 

# You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).

# You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.

# You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

# Example 1:

# Input: 
# [
#  [1,2,3],
#  [0,0,4],
#  [7,6,5]
# ]
# Output: 6
 

# Example 2:

# Input: 
# [
#  [1,2,3],
#  [0,0,0],
#  [7,6,5]
# ]
# Output: -1
 

# Example 3:

# Input: 
# [
#  [2,3,4],
#  [0,0,5],
#  [8,7,6]
# ]
# Output: 6
# Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.

# bfs TLE
def cutOffTree(self, forest):
    lx = len(forest)
    ly = len(forest[0])

    def bfs(s1, s2, t1, t2):
        queue = collections.deque([(s1, s2, 0)])
        seen = set([(s1, s2)])

        while queue:
            x, y, s = queue.popleft()
            seen.add((x, y))
            if x == t1 and y == t2: return s
            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                if 0 <= x + dx < lx and 0 <= y + dy < ly and forest[x + dx][y + dy] != 0 and (x + dx, y + dy) not in seen:
                    queue.append((x + dx, y + dy, s + 1))

        return -1

    route = sorted([(v, x, y) for x, t in enumerate(forest) for y, v in enumerate(t) if v > 1])
    cx = cy = 0
    res = 0

    for i, node in enumerate(route):
        _, nx, ny = node
        temp = bfs(cx, cy, nx, ny)

        if temp >= 0:
            res += temp
        else:
            return -1

        cx, cy = nx, ny

    return res