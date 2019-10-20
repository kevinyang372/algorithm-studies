# There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

# Note:
# All costs are positive integers.

# Example:

# Input: [[17,2,17],[16,16,5],[14,3,19]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
#              Minimum cost: 2 + 5 + 3 = 10.

# dp
def minCost(self, costs):
    cache = {}
    
    def search(i, prev):
        if i == len(costs): return 0
        if (i, prev) in cache: return cache[i, prev]
        
        min_val = float('inf')
        for ind, val in enumerate(costs[i]):
            if ind != prev:
                min_val = min(search(i + 1, ind) + val, min_val)
        
        cache[i, prev] = min_val
        return min_val
    
    return search(0, None)