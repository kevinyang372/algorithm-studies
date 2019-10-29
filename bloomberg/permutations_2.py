# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# Example:

# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

def permuteUnique(self, nums):
    c = collections.Counter(nums)
    
    def traverse(i, counter):
        if i == len(nums): return [[]]
        res = []
        for t in counter:
            if counter[t] > 0:
                counter[t] -= 1
                res += [[t] + m for m in traverse(i + 1, counter)]
                counter[t] += 1
                
        return res
    
    return traverse(0, c)