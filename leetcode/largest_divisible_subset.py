# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

# Si % Sj = 0 or Sj % Si = 0.

# If there are multiple solutions, return any subset is fine.

# Example 1:

# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)
# Example 2:

# Input: [1,2,4,8]
# Output: [1,2,4,8]

def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    
    if not nums: return []
    
    nums.sort()    
    visited = {}
    
    def search(i):
        if i in visited: return visited[i]
        maxv = [nums[i]]
        for j in range(i + 1, len(nums)):
            if nums[j] % nums[i] == 0:
                maxv = max([maxv, [nums[i]] + search(j)], key = len)
        visited[i] = maxv
        return maxv
    
    maxv = []
    for i in range(len(nums)):
        if i not in visited:
            maxv = max([maxv, search(i)], key = len)
            
    return maxv