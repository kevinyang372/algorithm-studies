# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.

def exist(board, word):

    if not board:
        return False
    elif not word:
        return True

    for k1, i1 in enumerate(board):
        for k2, i2 in enumerate(i1):
            if i2 == word[0]:
                if exist_from_point(board, word[1:], [k1, k2]): return True

    return False

def exist_from_point(board, word, point, visited = []):

    if len(word) == 0: return True

    t1, t2 = point
    visited += [point]

    h = len(board) 
    w = len(board[0])

    if t1 > 0 and [t1 - 1, t2] not in visited and board[t1 - 1][t2] == word[0]:
        if exist_from_point(board, word[1:], [t1 - 1, t2], visited): return True

    if t1 < h - 1 and [t1 + 1, t2] not in visited and board[t1 + 1][t2] == word[0]:
        if exist_from_point(board, word[1:], [t1 + 1, t2], visited): return True

    if t2 > 0 and [t1, t2 - 1] not in visited and board[t1][t2 - 1] == word[0]:
        if exist_from_point(board, word[1:], [t1, t2 - 1], visited): return True

    if t2 < w - 1 and [t1, t2 + 1] not in visited and board[t1][t2 + 1] == word[0]:
        if exist_from_point(board, word[1:], [t1, t2 + 1], visited): return True

    return False


