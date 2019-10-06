# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

def search(nums, target):

    if not nums: return -1

    if nums[-1] > nums[0]: return binary_search(nums, target)

    mid = len(nums) // 2

    if target == nums[mid]:
        return target

    if nums[mid] > nums[0]:
        if target < nums[mid] and target >= nums[0]:
            temp = binary_search(nums[:mid], target)
            if temp < 0:
                return -1
            else:
                return mid + temp + 1
        else:
            return mid + search(nums[mid + 1:], target)
    else:
        if target > nums[mid] and target <= nums[-1]:
            temp = binary_search(nums[mid + 1:], target)
            if temp < 0:
                return -1
            else:
                return mid + temp + 1
        else:
            return search(nums[:mid], target)




def binary_search(nums, target):
        
    first = -1
    last = len(nums)

    while first < last - 1:

        mid = (first + last) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            first = mid
        else:
            last = mid

    return -1
        
