# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

# Note:

# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Example 2:

# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]

# backtracking
def combinationSum3(self, k, n):
    if k > n or 9 * k < n or k > 9: return []
    
    def search(remaining, k, curr):
        if remaining == 0 and k == 0: return [[]]
        if remaining == 0 or k == 0: return False
        
        temp = []
        for i in range(curr + 1, 11 - k):
            if remaining - i < 0:
                break
            res = search(remaining - i, k - 1, i)
            
            if res != False:
                temp += [[i] + t for t in res]
        
        return temp
    
    return search(n, k, 0)