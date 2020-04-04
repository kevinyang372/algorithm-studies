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

# inplace O(N)

def moveZeroes(self, nums):
    if not nums: return
    
    i = j = 0
    while j < len(nums):
        if j == i and nums[j] != 0:
            j += 1
            i += 1
        elif nums[j] == 0:
            j += 1
        elif j > i and nums[j] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
            j += 1
            
    return nums

def moveZeroes(self, nums: List[int]) -> None:
    i = j = 0
    
    while i < len(nums) and nums[i] == 0 :
        i += 1
    
    while j < len(nums) and nums[j] != 0:
        j += 1
    
    if i == len(nums) or j == len(nums): return nums
    
    while i < len(nums):
        if nums[i] == 0:
            i += 1
            continue
        
        if j < i:
            nums[i], nums[j] = nums[j], nums[i]
            while j < len(nums) and nums[j] != 0:
                j += 1
                
        i += 1
    
    return nums
