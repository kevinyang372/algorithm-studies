# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# Example:

# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

def generateMatrix(n):
    res = [[0] * n for _ in range(n)]
    curr = 1
    
    left, right, up, down = 0, n - 1, 0, n - 1
    x = y = 0
    direction = 0
    
    while curr <= n ** 2:
        res[x][y] = curr

        if direction == 0 and y == right:
            direction = (direction + 1) % 4
            up = x + 1
        elif direction == 1 and x == down:
            direction = (direction + 1) % 4
            right = y - 1
        elif direction == 2 and y == left:
            direction = (direction + 1) % 4
            down = x - 1
        elif direction == 3 and x == up:
            direction = (direction + 1) % 4
            left = y + 1

        if direction == 0:
            y += 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y -= 1
        else:
            x -= 1
            
        curr += 1
    
    return res

def generateMatrix(self, n: int) -> List[List[int]]:
    matrix = [[0] * n for _ in range(n)]
    
    def next_direction(i, j, direction):
        d = {
            0: (0, 1),
            1: (1, 0),
            2: (0, -1),
            3: (-1, 0)
        }
        
        di, dj = d[direction]
        if 0 <= i + di < n and 0 <= j + dj < n and matrix[i + di][j + dj] == 0:
            return i + di, j + dj, direction
        else:
            direction = (direction + 1) % 4
            di, dj = d[direction]
            return i + di, j + dj, direction
    
    curr = (1, 0, 0, 0)
    matrix[0][0] = 1
    
    while curr[0] < n ** 2:
        val, i, j, direction = curr
        
        next_i, next_j, next_d = next_direction(i, j, direction)
        val += 1
        
        matrix[next_i][next_j] = val
        curr = (val, next_i, next_j, next_d)
    
    return matrix