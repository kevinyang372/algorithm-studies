# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# Your algorithm should run in O(n) complexity.

# Example:

# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# hashset (constant time lookup)
def longestConsecutive(self, nums):
        
    longest_streak = 0
    nums = set(nums)
    
    for i in nums:
        if i - 1 not in nums:
            current_streak = 1
            temp = i + 1
            
            while temp in nums:
                current_streak += 1
                temp += 1
                
            longest_streak = max(longest_streak, current_streak)
    
    return longest_streak