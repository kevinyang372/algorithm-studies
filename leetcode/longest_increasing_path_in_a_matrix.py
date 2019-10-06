# Given an integer matrix, find the length of the longest increasing path.

# From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

# Example 1:

# Input: nums = 
# [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [1, 2, 6, 9].
# Example 2:

# Input: nums = 
# [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

def longestIncreasingPath(matrix):

    if not matrix: return 0

    max_path = 0
    for m in range(len(matrix)):
        for n in range(len(matrix[0])):
            max_path = max(max_path, longest_from_point(m, n, matrix))

    return max_path

cache = {}

def longest_from_point(row, col, matrix):

    if (row, col) in cache: return cache[(row, col)]

    count = 1

    if row > 0:
        if matrix[row - 1][col] > matrix[row][col]: count = max(count, 1 + longest_from_point(row - 1, col, matrix))

    if col > 0:
        if matrix[row][col - 1] > matrix[row][col]: count = max(count, 1 + longest_from_point(row, col - 1, matrix))

    if row < len(matrix) - 1:
        if matrix[row + 1][col] > matrix[row][col]: count = max(count, 1 + longest_from_point(row + 1, col, matrix))

    if col < len(matrix[0]) - 1:
        if matrix[row][col + 1] > matrix[row][col]: count = max(count, 1 + longest_from_point(row, col + 1, matrix))

    cache[(row, col)] = count
    return count



