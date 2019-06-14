# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]

def findDisappearedNumbers(nums):
    full = [i for i in range(1, len(nums) + 1)]
    return list(set(full) - set(nums))

# O(N) time and O(1) Space

def findDisappearedNumbers(nums):
    for num in nums:
        index = abs(num) - 1
        nums[index] = - abs(nums[index])

    return [i + 1 for i, num in enumerate(nums) if num > 0]