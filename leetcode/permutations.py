# Given a collection of distinct integers, return all possible permutations.

# Example:

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

def permute(nums):

    if len(nums) == 0: return []
    elif len(nums) == 1: return [nums]

    res = []
    for i in range(len(nums)):
        temp = nums[i]
        res += [[temp] + t for t in permute(nums[:i] + nums[i + 1:])]

    return res

