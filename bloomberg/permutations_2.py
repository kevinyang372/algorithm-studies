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


# backtracking
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
    c = collections.Counter(nums)
    def create_permutation(c):
        if len(c) == 0: return [[]]
        
        res = []
        k = list(c.keys())
        
        for key in k:
            c[key] -= 1
            if c[key] == 0: del c[key]
            res.extend([[key] + l for l in create_permutation(c)])
            c[key] += 1
        
        return res
    
    return create_permutation(c)