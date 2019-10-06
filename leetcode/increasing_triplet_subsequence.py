# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

# Formally the function should:

# Return true if there exists i, j, k 
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
# Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

# Example 1:

# Input: [1,2,3,4,5]
# Output: true
# Example 2:

# Input: [5,4,3,2,1]
# Output: false

def increasingTriplet(nums):

    if len(nums) < 2: return False

    minimum = [float('inf'), float('inf')]

    for i in nums:
        if i > minimum[0] and i > minimum[1]:
            return True
        elif i < minimum[0]:
            minimum[0] = i
        elif i > minimum[0] and i < minimum[1]:
            minimum[1] = i

    return False

