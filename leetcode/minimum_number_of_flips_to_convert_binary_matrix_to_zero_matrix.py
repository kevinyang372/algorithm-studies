# Given a m x n binary matrix mat. In one step, you can choose one cell and flip it and all the four neighbours of it if they exist (Flip is changing 1 to 0 and 0 to 1). A pair of cells are called neighboors if they share one edge.

# Return the minimum number of steps required to convert mat to a zero matrix or -1 if you cannot.

# Binary matrix is a matrix with all cells equal to 0 or 1 only.

# Zero matrix is a matrix with all cells equal to 0.

 

# Example 1:


# Input: mat = [[0,0],[0,1]]
# Output: 3
# Explanation: One possible solution is to flip (1, 0) then (0, 1) and finally (1, 1) as shown.
# Example 2:

# Input: mat = [[0]]
# Output: 0
# Explanation: Given matrix is a zero matrix. We don't need to change it.
# Example 3:

# Input: mat = [[1,1,1],[1,0,1],[0,0,0]]
# Output: 6
# Example 4:

# Input: mat = [[1,0,0],[1,0,0]]
# Output: -1
# Explanation: Given matrix can't be a zero matrix
 

# Constraints:

# m == mat.length
# n == mat[0].length
# 1 <= m <= 3
# 1 <= n <= 3
# mat[i][j] is 0 or 1.

def minFlips(self, mat: List[List[int]]) -> int:
        
    m, n = len(mat), len(mat[0])
    
    def convert_1d_2d(i):
        return i // n, i % n
    
    def convert_2d_1d(x, y):
        return x * n + y
    
    flatten = []
    for l in mat:
        flatten += l
        
    goal = tuple([0] * (m * n))
    queue = collections.deque([(tuple(flatten), 0)])
    visited = set()
    
    while queue:
        curr, cost = queue.popleft()
        visited.add(curr)
        
        if curr == goal: return cost
        
        for ind in range(len(curr)):
            temp = list(curr)
            
            x, y = convert_1d_2d(ind)
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0], [0, 0]]:
                if 0 <= x + dx < m and 0 <= y + dy < n:
                    i = convert_2d_1d(x + dx, y + dy)
                    temp[i] = 1 - temp[i]
                    
            temp = tuple(temp)
            if temp not in visited:
                queue.append((temp, cost + 1))
    
    return -1