# Given an array, rotate the array to the right by k steps, where k is non-negative.

def rotate(nums, k):

    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]