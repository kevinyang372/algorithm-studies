# Given a sorted integer array without duplicates, return the summary of its ranges.

# Example 1:

# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
# Example 2:

# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

def summaryRanges(self, nums):
        
    stack = []
    
    for i in nums:
        if not stack or i > stack[-1][1] + 1:
            stack.append([i, i])
        else:
            stack[-1][1] = i
    
    res = []
    for x, y in stack:
        if x == y:
            res.append(str(x))
        else:
            res.append("%s->%s" % (x, y))
            
    return res

def summaryRanges(self, nums: List[int]) -> List[str]:
    res = []
    
    i = 0
    while i < len(nums):
        j = i + 1
        
        while j < len(nums) and nums[j] == nums[j - 1] + 1:
            j += 1
        
        if i != j - 1:
            res.append(f"{nums[i]}->{nums[j - 1]}")
        else:
            res.append(f"{nums[i]}")
        
        i = j
    
    return res