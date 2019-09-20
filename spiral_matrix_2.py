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