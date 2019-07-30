# Given an array return an integer indicating the minimum number of swap operations required to sort the array into ascending order.

# Example 1:

# Input: [5, 1, 3, 2]
# Output: 2
# Explanation: [5, 1, 3, 2] -> [2, 1, 3, 5] - > [1, 2, 3, 5]
# Example 2:

# Input: [1, 3, 2]
# Output: 1
# Explanation: [1, 3, 2] -> [1, 2, 3]

def minSwaps(nums):

    nums = [*enumerate(nums)]
    nums.sort(key = lambda x: x[1])

    visited = set()
    swaps = 0

    for i, v in enumerate(nums):
        if i == v[0]:
            continue

        start = v[0]
        node = 1
        visited.add(i)

        while start not in visited:
            visited.add(start)
            start = nums[start][0]
            node += 1

        swaps += node - 1

    return swaps
