# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

# You are given a target value to search. If found in the array return true, otherwise return false.

# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# Follow up:

# This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
# Would this affect the run-time complexity? How and why?

def search(self, nums, target):
    if not nums: return False
    
    def binary_search(nums, target):
    
        first = -1
        last = len(nums)

        while first < last - 1:

            mid = (first + last) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                first = mid
            else:
                last = mid

        return False

    if nums[-1] > nums[0]: return binary_search(nums, target)

    mid = len(nums) // 2

    if target == nums[mid]:
        return True

    if nums[mid] == nums[0]:
        return self.search(nums[mid + 1:], target) or self.search(nums[:mid], target)
    elif nums[mid] > nums[0]:
        if target < nums[mid] and target >= nums[0]:
            return binary_search(nums[:mid], target)
        else:
            return self.search(nums[mid + 1:], target)
    else:
        if target > nums[mid] and target <= nums[-1]:
            return binary_search(nums[mid + 1:], target)
        else:
            return self.search(nums[:mid], target)