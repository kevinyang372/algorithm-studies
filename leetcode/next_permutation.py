# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place and use only constant extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

def nextPermutation(nums):

    if len(nums) < 2: return nums

    i = len(nums) - 1
    min_stack = []
    
    while i > 0:
        min_stack = [nums[i]] + min_stack
        if nums[i] > nums[i - 1]:
            for t in range(len(min_stack)):
                if min_stack[t] <= nums[i - 1]:
                    min_stack[t - 1], nums[i - 1] = nums[i - 1], min_stack[t - 1]
                    break
                elif t == len(min_stack) - 1:
                    min_stack[t], nums[i - 1] = nums[i - 1], min_stack[t]
            break
        i -= 1  
    
    if i == 0:
        nums.reverse()
    else:
        nums[i:] = reversed(min_stack)


# O(1) Space

def nextPermutation(nums):
        
    if not nums: return
    
    j = len(nums) - 1
    
    while j > 0:
        if nums[j] > nums[j - 1]:
            temp = j - 1
            while j < len(nums) and nums[j] > nums[temp]:
                j += 1
            nums[temp], nums[j - 1] = nums[j - 1], nums[temp]
            nums[temp + 1:] = nums[temp + 1:][::-1]
            return
        j -= 1
        
    nums.reverse()
    return