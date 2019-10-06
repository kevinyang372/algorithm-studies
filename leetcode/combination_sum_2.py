# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

# Each number in candidates may only be used once in the combination.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]

def combinationSum2(self, candidates, target):
        
    res = set()
    d = collections.defaultdict(list)
    d[0] = [[]]
    
    for i in candidates:
        if i > target:
            continue
        if target - i in d:
            for ind in d[target - i]:
                res.add(tuple(sorted(ind + [i])))
        
        for m in reversed(range(target - i)):
            if m in d:
                d[m + i] += [t + [i] for t in d[m]]
                
    return list(res)