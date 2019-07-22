# The encoder can merge only two files at a time. The time required to merge the two files is equal to the sum of their sizes. The size of this merged file is also equal to the sum of their sizes. The process is repeated until the N sub files are merged into a single output file.

# Write an algorithm to output the minimum possible time to merge the given N subfiles into a single file

# Example 1:

# Input: numOfSubFiles = 4, files = [20, 4, 8, 2]
# Output: 54
# Example 2:

# Input: numOfSubFiles = 6, files = [1, 2, 5, 10, 35, 89]
# Output: 224
# Example 3:

# Input: numOfSubFiles = 4, files = [2, 2, 3, 3]
# Output: 20

import heapq
def minimumTime(files):

    heapq.heapify(files)
    sums = 0

    while len(files) > 1:
        h1 = heapq.heappop(files)
        h2 = heapq.heappop(files)

        sums += h1 + h2

        heapq.heappush(files, h1 + h2)

    return sums