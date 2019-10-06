# There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].
# 
# Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.
# 
#  
# 
# Example 1:
# 
# Input: [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation: 
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.
# 
# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
#  
# 
# Note:
# 
# 1 <= costs.length <= 100
# It is guaranteed that costs.length is even.
# 1 <= costs[i][0], costs[i][1] <= 1000

def twoCitySchedCost(self, costs):
        
        length = len(costs)
        cache = {}
        
        def findMin(ind, A, B):
            if (ind, A, B) in cache: return cache[ind, A, B]
            if ind == length: return 0
            if B == 0:
                res = costs[ind][0] + findMin(ind + 1, A - 1, B)
            elif A == 0:
                res = costs[ind][1] + findMin(ind + 1, A, B - 1)
            else:
                res = min(costs[ind][0] + findMin(ind + 1, A - 1, B), costs[ind][1] + findMin(ind + 1, A, B - 1))
            
            cache[ind, A, B] = res
            return res
        
        return findMin(0, length / 2, length / 2)
