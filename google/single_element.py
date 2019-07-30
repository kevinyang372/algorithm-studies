# Given an array nums of length n. All elements appear in pairs except one of them. Find this single element that appears alone.
# Pairs of the same element cannot be adjacent:

# [2, 2, 1, 2, 2] // ok
# [2, 2, 2, 2, 1] // not allowed
# Example 1:

# Input: [2, 2, 1, 1, 9, 9, 5, 2, 2]
# Output: 5
# Example 2:

# Input: [1, 1, 2]
# Output: 2
# Example 3:

# Input: [3, 3, 2, 3, 3]
# Output: 2

def singleElement(nums):

    if len(nums) == 3: return nums[0] if nums[0] != nums[1] else nums[-1]
    i, j = 0, len(nums) - 1

    while i <= j:

        mid = (i + j) // 2

        if mid == len(nums) - 1 or nums[mid] != nums[mid - 1]:
            return nums[mid]
        elif nums[mid] != nums[mid - 1]:
            i = mid + 1
        else:
            j = mid

    return None