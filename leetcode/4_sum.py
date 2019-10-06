# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note:

# The solution set must not contain duplicate quadruplets.

# Example:

# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

def fourSum(self, nums, target):
    results = []
    self.nSum(sorted(nums), target, 4, [], results)
    return results

def nSum(self, nums, target, N, result, results):
    if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N: return 

    for i in range(len(nums) - N + 1):
        if i == 0 or nums[i] != nums[i - 1]:
            if N == 3:
                self.twoSum(nums[i + 1:], target - nums[i], result + [nums[i]], results)
            else:
                self.nSum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)

def twoSum(self, nums, target, result, results):
    i, j = 0, len(nums) - 1
    while i < j:
        s = nums[i] + nums[j]
        if s == target:
            results.append(result + [nums[i], nums[j]])
            i += 1

            while i < j and nums[i] == nums[i - 1]:
                i += 1
        elif s < target:
            i += 1
        else:
            j -= 1