# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

def subsetsWithDup(self, nums):
        
    nums.sort()
    
    def subset(nums):
        if not nums:
            temp = set()
            temp.add(())
            return temp
        
        head = nums[0]
        res = subset(nums[1:])
        
        m = set()
        for i in res:
            temp = list(i)
            temp.append(head)
            m.add(tuple(temp))
        
        res.update(m)
        return res
    
    return [list(i) for i in subset(nums)]