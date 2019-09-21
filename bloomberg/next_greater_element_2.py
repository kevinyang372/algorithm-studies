# Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

# Example 1:
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number; 
# The second 1's next greater number needs to search circularly, which is also 2.
# Note: The length of given array won't exceed 10000.

# stack approach
def nextGreaterElements(self, nums):
        
    res = [0] * len(nums)
    stack = []
    
    for _ in range(2):
        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()

            if stack:
                res[i] = stack[-1]
            else:
                res[i] = -1

            stack.append(nums[i])
            
    return res