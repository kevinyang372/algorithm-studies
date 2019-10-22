# Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

# Example:

# Input: nums = [-2,0,1,3], and target = 2
# Output: 2 
# Explanation: Because there are two triplets which sums are less than 2:
#              [-2,0,1]
#              [-2,0,3]
# Follow up: Could you solve it in O(n2) runtime?

def threeSumSmaller(self, nums, target):
    nums.sort()
    res = 0
    
    for i in range(2, len(nums)):
        if nums[i] + nums[0] + nums[1] > target:
            break
        
        t, j = 0, i - 1
        search = target - nums[i]
        
        while j > t:
            if nums[j] + nums[t] < search:
                res += j - t
                t += 1
            else:
                j -= 1
                
    return res