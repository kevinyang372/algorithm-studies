# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# hashmap TLE
def threeSum(nums):
    res = set()
    d = collections.defaultdict(set)
    
    for i in range(1, len(nums)):
        if -nums[i] in d:
            for m in d[-nums[i]]:
                temp = sorted(list(m) + [nums[i]])
                res.add(tuple(temp))
        for t in range(i):
            d[nums[i] + nums[t]].add((nums[i], nums[t]))
            
    return list(res)

# two pointers
def threeSum(nums):
    if len(nums) < 3: return
    
    nums.sort()
    res = []
    
    for i in range(len(nums) - 2):
        
        if nums[i] > 0: break
        if i > 0 and nums[i] == nums[i - 1]: continue
            
        r, j = i + 1, len(nums) - 1
        
        while r < j:
            total = nums[i] + nums[r] + nums[j]
            if total > 0:
                j -= 1
            elif total < 0:
                r += 1
            else:
                res.append([nums[i], nums[r], nums[j]])
                
                while r < j and nums[r] == nums[r + 1]:
                    r += 1
                while r < j and nums[j] == nums[j - 1]:
                    j -= 1
                    
                r += 1
                j -= 1
    
    return res