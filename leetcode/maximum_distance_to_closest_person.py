# In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

# There is at least one empty seat, and at least one person sitting.

# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

# Return that maximum distance to closest person.

# Example 1:

# Input: [1,0,0,0,1,0,1]
# Output: 2
# Explanation: 
# If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
# Example 2:

# Input: [1,0,0,0]
# Output: 3
# Explanation: 
# If Alex sits in the last seat, the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
# Note:

# 1 <= seats.length <= 20000
# seats contains only 0s or 1s, at least one 0, and at least one 1.

# two passes
def maxDistToClosest(self, seats):
    d = [float('inf')] * len(seats)
    
    for i in range(1, len(seats)):
        if seats[i] == 1:
            d[i] = 0
        elif seats[i - 1] == 1:
            d[i] = 1
        elif d[i - 1] < len(seats):
            d[i] = d[i - 1] + 1
            
    max_d = d[-1]
    d2 = [float('inf')] * len(seats)
    
    for i in range(len(seats) - 2, -1, -1):
        if seats[i] == 1:
            d2[i] = 0
            continue
        elif seats[i + 1] == 1:
            d2[i] = 1
            max_d = max(max_d, 1)
        else:
            d2[i] = d2[i + 1] + 1
            temp = min(d[i], d2[i])
            max_d = max(max_d, temp)
            
    return max_d

# one pass
def maxDistToClosest(self, seats):

    left, count, max_d = -1, 0, 1

    for i, v in enumerate(seats):
        if v == 0:
            count += 1
        else:
            if left < 0:
                distance = count
            else:
                distance = count // 2 + count % 2

            left = i
            count = 0
            max_d = max(max_d, distance)

    return max(max_d, count)