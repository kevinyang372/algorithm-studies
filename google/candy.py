# There are N children standing in a line. Each child is assigned a rating value.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?

# Example 1:

# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# Example 2:

# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
#              The third child gets 1 candy because it satisfies the above two conditions.

# two passes
def candy(self, ratings):
        
    candies = [1] * len(ratings)
    
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    
    sums = candies[-1]
    for t in range(len(ratings) - 2, -1, -1):
        if ratings[t] > ratings[t + 1]:
            candies[t] = max(candies[t], candies[t + 1] + 1)
        sums += candies[t]

    return sums