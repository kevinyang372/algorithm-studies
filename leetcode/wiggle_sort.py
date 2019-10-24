# Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

# Example:

# Input: nums = [3,5,2,1,6,4]
# Output: One possible answer is [3,5,1,6,2,4]

def wiggleSort(self, nums):
    t = 1
    while t < len(nums):
        if t > 0 and (t % 2 == 0 and nums[t] > nums[t - 1]) or (t % 2 == 1 and nums[t] < nums[t - 1]):
            nums[t], nums[t - 1] = nums[t - 1], nums[t]
            t -= 1
        else:
            t += 1
    
    return nums