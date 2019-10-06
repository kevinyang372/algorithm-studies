# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

# Example 1:

# Input: [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: [3,1,3,4,2]
# Output: 3
# Note:

# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.

# Memory O(N) Time O(N)
def findDuplicate(nums):

    ind = [False] * (len(nums) - 1)

    for i in nums:
        if ind[i - 1]:
            return i
        ind[i - 1] = True

# The data structure could be thought as a linked list
# If duplicate exists, then there exists cycle in the linked list
# Memory O(N) Time
def findDuplicate(nums):

    slow = nums[0]
    fast = nums[nums[0]]

    while slow != fast:
        slow, fast = nums[slow], nums[nums[fast]]

    fast = 0

    while slow != fast:
        slow, fast = nums[slow], nums[fast]

    return fast