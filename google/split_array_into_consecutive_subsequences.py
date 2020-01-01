# Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

 

# Example 1:

# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3
# 3, 4, 5

# Example 2:

# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3, 4, 5
# 3, 4, 5

# Example 3:

# Input: [1,2,3,4,4,5]
# Output: False
 

# Constraints:

# 1 <= nums.length <= 10000

def isPossible(self, nums):
        
    stack = []
    ind = 0
    pre = None
    
    while ind < len(nums):

        if pre and nums[ind] != pre + 1:
            if any([v < 3 for v in stack]): return False
            stack = []
        
        pre = nums[ind]
        t = ind
        while t < len(nums) - 1 and nums[t] == nums[t + 1]:
            t += 1
        
        count = t - ind + 1
        if count >= len(stack):
            stack = [v + 1 for v in stack] + [1] * (count - len(stack))
        else:
            qualified, unqualified = [], []
            for v in stack:
                if v >= 3:
                    qualified.append(v)
                else:
                    unqualified.append(v)
                    
            if len(qualified) < len(stack) - count:
                return False
            else:
                temp = unqualified + qualified[len(stack) - count:]
                stack = [v + 1 for v in temp]
        
        ind = t + 1
    
    return all([v >= 3 for v in stack])