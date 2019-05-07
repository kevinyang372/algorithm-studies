# Shuffle a set of numbers without duplicates.

# Example:

# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);

# // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
# solution.shuffle();

# // Resets the array back to its original configuration [1,2,3].
# solution.reset();

# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();

import random

class Solution:

    def __init__(self, nums):
        self.origin = nums
        self.current = nums

    def reset(self):
        return self.origin

    def shuffle(self):
        rank = random.sample(range(len(self.current) + 1), len(self.current))
        temp_rank = rank[:]
        new_current = []

        while len(temp_rank) > 0:
            min_value = min(temp_rank)
            min_index = rank.index(min_value)
            temp_rank.pop(temp_rank.index(min_value))
            new_current.append(self.current[min_index])

        self.current = new_current
        return self.current