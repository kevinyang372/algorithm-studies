# Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

# Example:

# Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# Output: ["2", "4->49", "51->74", "76->99"]

def findMissingRanges(self, nums, lower, upper):
    nums = [lower - 1] + nums
    nums.append(upper + 1)
    stack = []
    
    for i in range(1, len(nums)):

        start, end = nums[i - 1], nums[i]
        
        if end - start == 2:
            stack.append(str(end - 1))
        elif end - start > 2:
            stack.append("%s->%s" % (start + 1, end - 1))
    
    return stack