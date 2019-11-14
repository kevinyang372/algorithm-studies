# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

# Example 1:
# Input: [3, 2, 1]

# Output: 1

# Explanation: The third maximum is 1.
# Example 2:
# Input: [1, 2]

# Output: 2

# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
# Example 3:
# Input: [2, 2, 3, 1]

# Output: 1

# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.

def thirdMax(self, nums):
        
    if not nums: return
    
    maxs = [-float('inf'), -float('inf'), -float('inf')]
    
    for i in nums:
        for t in range(len(maxs)):
            if i > maxs[t]:
                ind, cur = t, maxs[t]
                while ind + 1 < len(maxs):
                    cur, maxs[ind + 1] = maxs[ind + 1], cur
                    ind += 1
                
                maxs[t] = i
                break
            elif i == maxs[t]:
                break
    
    return maxs[-1] if maxs[-1] != -float('inf') else maxs[0]