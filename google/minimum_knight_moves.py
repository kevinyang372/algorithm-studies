# In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

# A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.



# Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

 

# Example 1:

# Input: x = 2, y = 1
# Output: 1
# Explanation: [0, 0] → [2, 1]
# Example 2:

# Input: x = 5, y = 5
# Output: 4
# Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 

# Constraints:

# |x| + |y| <= 300

# bfs
def minKnightMoves(self, x, y):
        
    queue = collections.deque([(0, 0)])
    cost = {}
    cost[0, 0] = 0
    
    while queue:
        cx, cy = queue.popleft()
        if cx == x and cy == y: return cost[cx, cy]
        
        for dx, dy in [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]:
            if cost.get((dx + cx, dy + cy), float('inf')) > cost[cx, cy] + 1:
                cost[dx + cx, dy + cy] = cost[cx, cy] + 1
                queue.append((dx + cx, dy + cy))
        
    return -1

