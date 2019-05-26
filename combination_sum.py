# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

# The same repeated number may be chosen from candidates unlimited number of times.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:

# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

def combinationSum(candidates, target: int):

    if target < min(candidates):
        return []

    result = []
    for i in candidates:
        if i < target:
            temp = combinationSum(candidates, target - i)

            if temp:
                for t in temp:
                    result.append(sorted([i] + t))
        elif i == target:
            result.append([i])

    k = sorted(result)
    result = [k[i] for i in range(len(k)) if i == 0 or k[i] != k[i-1]]

    return result

# def combinationSum_dfs(candidates, target: int):

#     result = {}
#     stack = [[target, None]]

#     while len(stack) > 0:
        
#         node = stack.pop()
        
#         for i in candidates:
#             if node[0] > i:

