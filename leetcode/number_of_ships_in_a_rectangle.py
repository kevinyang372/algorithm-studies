# On the sea represented by a cartesian plane, each ship is located at an integer point, and each integer point may contain at most 1 ship.

# You have a function Sea.hasShips(topRight, bottomLeft) which takes two points as arguments and returns true if and only if there is at least one ship in the rectangle represented by the two points, including on the boundary.

# Given two points, which are the top right and bottom left corners of a rectangle, return the number of ships present in that rectangle.  It is guaranteed that there are at most 10 ships in that rectangle.

# Submissions making more than 400 calls to hasShips will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

# Example :



# Input: 
# ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
# Output: 3
# Explanation: From [0,0] to [4,4] we can count 3 ships within the range.
 

# Constraints:

# On the input ships is only given to initialize the map internally. You must solve this problem "blindfolded". In other words, you must find the answer using the given hasShips API, without knowing the ships position.
# 0 <= bottomLeft[0] <= topRight[0] <= 1000
# 0 <= bottomLeft[1] <= topRight[1] <= 1000

# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight, bottomLeft):
#        """
#        :type topRight: Point
#        :type bottomLeft: Point
#        :rtype bool
#        """
#
#class Point(object):
#   def __init__(self, x, y):
#       self.x = x
#       self.y = y

class Solution(object):    
    def countShips(self, sea, topRight, bottomLeft):
        if not sea.hasShips(topRight, bottomLeft): return 0
        
        total = 0
        stack = collections.deque([(topRight, bottomLeft)])
        
        while stack:
            if len(stack) + total >= 10: return 10
            up, lo = stack.popleft()
            print(up.x, up.y, lo.x, lo.y)
            
            mid_x = (up.x + lo.x + 1) // 2
            mid_y = (up.y + lo.y + 1) // 2
            
            for dx, dy in [[up, Point(mid_x, mid_y)], [Point(mid_x - 1, up.y), Point(lo.x, mid_y)], [Point(mid_x - 1, mid_y - 1), lo], [Point(up.x, mid_y - 1), Point(mid_x, lo.y)]]:
                if dx.x < dy.x or dx.y < dy.y: continue
                if not sea.hasShips(dx, dy): continue
                if dx.x == dy.x and dx.y == dy.y:
                    total += 1
                    continue
                
                stack.append([dx, dy])
            
        return total