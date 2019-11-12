# Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

 

# Example 1:

# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
 

# Note:

# 1 <= k <= len(nums) <= 16.
# 0 < nums[i] < 10000.

def canPartitionKSubsets(self, nums, k):
        
    sums = sum(nums)
    
    if sums % k != 0: return False
    target = sums // k
    
    nums = collections.Counter(nums)
    
    def backtracking(subset):
        
        if sum([i * subset[i] for i in subset]) == target: return True
        
        s = collections.Counter(subset)
        options = findsubsets(s, target)
        if not options: return False
        
        for option in options:
            if backtracking(s - collections.Counter(option)):
                return True
            
        return False
    
    def findsubsets(c, t):

        res = []
        if t == 0: res.append([])
        visited = set()

        for i in c:
            if c[i] > 0:
                c[i] -= 1
                for m in findsubsets(c, t - i):
                    if tuple(sorted([i] + m)) not in visited:
                        res.append([i] + m)
                        visited.add(tuple(sorted([i] + m)))
                c[i] += 1

        return res
    
    return backtracking(nums)