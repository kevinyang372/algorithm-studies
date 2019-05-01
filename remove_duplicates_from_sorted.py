# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

def removeDuplicates(nums):

    i = 0

    while i < len(nums) - 1:

        if nums[i] == nums[i + 1]:
            nums[:] = nums[:i + 1] + nums[i + 2:]
            continue

        i += 1

    return len(nums)