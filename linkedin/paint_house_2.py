# There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

# Note:
# All costs are positive integers.

# Example:

# Input: [[1,5,3],[2,9,4]]
# Output: 5
# Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
#              Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5. 
# Follow up:
# Could you solve it in O(nk) runtime?

def minCostII(self, costs: List[List[int]]) -> int:
        
    if not costs: return 0
    if len(costs) == 1: return min(costs[0])
    
    dp = [[0] * len(costs[0]) for _ in range(len(costs) + 1)]
    
    for ind, cost in enumerate(costs):
        for i, v in enumerate(cost):
            dp[ind + 1][i] = min([dp[ind][t] for t in range(len(dp[ind])) if t != i]) + v
            
    return min(dp[-1])