# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

def removeDuplicates(nums):

    if not nums: return
    if len(nums) < 2: return len(nums)
    
    ind = 0
    
    while ind < len(nums) - 1:
        if nums[ind] == nums[ind + 1]:
            nums.pop(ind)
        else:
            ind += 1

    return len(nums)

# pop is unnecessary; faster
def removeDuplicates(self, nums):
        
    if len(nums) < 2: return len(nums)
    
    i = count = 0
    j = 1
    
    while j < len(nums):
        if nums[i] == nums[j]:
            j += 1
        else:
            nums[i + 1] = nums[j]
            i += 1
            j += 1
            count += 1
    
    return count + 1