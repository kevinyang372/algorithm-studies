# You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.

# paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.

# Also, there is no garden that has more than 3 paths coming into or leaving it.

# Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

# Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.  The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.

 

# Example 1:

# Input: N = 3, paths = [[1,2],[2,3],[3,1]]
# Output: [1,2,3]
# Example 2:

# Input: N = 4, paths = [[1,2],[3,4]]
# Output: [1,2,1,2]
# Example 3:

# Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
# Output: [1,2,3,4]
 

# Note:

# 1 <= N <= 10000
# 0 <= paths.size <= 20000
# No garden has 4 or more paths coming into or leaving it.
# It is guaranteed an answer exists.

# backtracking TLE
def gardenNoAdj(self, N, paths):
        
    if not paths: return [1] * N
    
    self.d = collections.defaultdict(int)
    self.connected = collections.defaultdict(list)
    
    for i in paths:
        self.connected[i[0]].append(i[1])
        self.connected[i[1]].append(i[0])
        
    self.slot = N
    self.solve()
    
    res = []
    for i in range(1, self.slot + 1):
        if i in self.d:
            res.append(self.d[i])
        else:
            res.append(1)
    
    return res
    
def solve(self):
    t = self.find_unsolved()
    if not t: return True
    
    for num in [1,2,3,4]:
         if self.isvalid(num, t):
            self.d[t] = num
            if self.solve():
                return True
            self.d[t] = 0
            
    return False
        
def isvalid(self, num, ind):
    for i in self.connected[ind]:
        if num == self.d[i]:
            return False
    return True
        
def find_unsolved(self):
    for t in self.connected:
        if self.d[t] == 0:
            return t
    return False