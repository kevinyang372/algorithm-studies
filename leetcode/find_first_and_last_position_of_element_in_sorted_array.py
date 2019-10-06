# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

def searchRange(nums, target):

    if not nums: return [-1, -1]
    if target < nums[0] or target > nums[-1]: return [-1, -1]
    if nums[0] == nums[-1] == target: return [0, len(nums) - 1]

    mid = len(nums) // 2

    if target > nums[mid]:
        i1, i2 = searchRange(nums[mid + 1:], target)
        if i1 == i2 == -1: return [-1, -1]
        return [mid + i1 + 1, mid + i2 + 1]
    elif target < nums[mid]:
        i1, i2 = searchRange(nums[:mid], target)
        if i1 == i2 == -1: return [-1, -1]
        return [i1, i2]
    else:
        i1, m2 = searchRange(nums[:mid], target)

        if i1 == -1:
            i1 = mid

        m1, i2 = searchRange(nums[mid + 1:], target)

        if i2 == -1:
            i2 = mid
        else:
            i2 += mid + 1

        return [i1, i2]
