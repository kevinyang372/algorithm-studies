# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

def contains_duplicates(nums):

    for i in range(len(nums)):
        if nums[i] in nums[:i]:
            return True

    return False