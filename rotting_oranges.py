# In a given grid, each cell can have one of three values:

# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

# Example 1:



# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

# Note:

# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.

def orangesRotting(self, grid):
        
    start = []
    count = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                count += 1
            elif grid[i][j] == 2:
                start.append((i, j))
                
    if count == 0:
        return 0
    elif len(start) == 0:
        return -1
    
    count += len(start)
    stack = collections.deque([[i, 0] for i in start])
    max_val = 0
    visited = set()
    
    while stack:
        (x, y), t = stack.popleft()
        max_val = max(max_val, t)
        count -= 1
        
        grid[x][y] = 2
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] == 1 and (x + dx, y + dy) not in visited:
                stack.append([(x + dx, y + dy), t + 1])
                visited.add((x + dx, y + dy))
        
    if count > 0:
        return -1
    
    return max_val