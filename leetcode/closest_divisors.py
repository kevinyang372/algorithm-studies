# Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.

# Return the two integers in any order.

 

# Example 1:

# Input: num = 8
# Output: [3,3]
# Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.
# Example 2:

# Input: num = 123
# Output: [5,25]
# Example 3:

# Input: num = 999
# Output: [40,25]
 

# Constraints:

# 1 <= num <= 10^9

def closestDivisors(self, num: int) -> List[int]:
        
    ans = [1, num + 1]
    
    for i in range(1, 3):
        curr = num + i
        for t in range(2, int(curr ** .5) + 1):
            if curr % t == 0 and abs(curr // t - t) < abs(ans[0] - ans[1]):
                ans = [t, curr // t]
    
    return ans