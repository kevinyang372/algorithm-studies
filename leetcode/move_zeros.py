# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

def moveZeroes(nums):

    count = 0
    ind = 0

    while count < len(nums):

        if nums[ind] == 0:
            nums.pop(ind)
            nums.append(0)
            ind -= 1

        ind += 1
        count += 1

