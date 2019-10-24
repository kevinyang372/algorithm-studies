# Given an array with n integers, you need to find if there are triplets (i, j, k) which satisfies following conditions:

# 0 < i, i + 1 < j, j + 1 < k < n - 1
# Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.
# where we define that subarray (L, R) represents a slice of the original array starting from the element indexed L to the element indexed R.
# Example:
# Input: [1,2,1,2,1,2,1]
# Output: True
# Explanation:
# i = 1, j = 3, k = 5. 
# sum(0, i - 1) = sum(0, 0) = 1
# sum(i + 1, j - 1) = sum(2, 2) = 1
# sum(j + 1, k - 1) = sum(4, 4) = 1
# sum(k + 1, n - 1) = sum(6, 6) = 1
# Note:
# 1 <= n <= 2000.
# Elements in the given array will be in range [-1,000,000, 1,000,000].

# O(N^3)
def splitArray(self, nums):
    if len(nums) < 7: return False

    d = {}
    sums = 0

    for i, v in enumerate(nums):
        sums += v
        d[i] = sums

    for k in range(5, len(nums) - 1):
        for j in range(3, k - 1):
            for i in range(1, j - 1):
                if d[i - 1] == (d[j - 1] - d[i]) == (d[k - 1] - d[j]) == (sums - d[k]):
                    return True
                
    return False

# O(N^2)
def splitArray(self, nums):
    if len(nums) < 7: return False

    d = {}
    sums = 0

    for i, v in enumerate(nums):
        sums += v
        d[i] = sums

    for j in range(3, len(nums) - 3):
        visited = set()
        for i in range(1, j - 1):
            if d[i - 1] == d[j - 1] - d[i]:
                visited.add(d[i - 1])
        
        for k in range(j + 2, len(nums) - 1):
            if d[len(nums) - 1] - d[k] == d[k - 1] - d[j] and d[k - 1] - d[j] in visited:
                return True

                
    return False