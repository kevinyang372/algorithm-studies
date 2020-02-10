# On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

# Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.



# We may make the following moves:

# 'U' moves our position up one row, if the position exists on the board;
# 'D' moves our position down one row, if the position exists on the board;
# 'L' moves our position left one column, if the position exists on the board;
# 'R' moves our position right one column, if the position exists on the board;
# '!' adds the character board[r][c] at our current position (r, c) to the answer.
# (Here, the only positions that exist on the board are positions with letters on them.)

# Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.

 

# Example 1:

# Input: target = "leet"
# Output: "DDR!UURRR!!DDD!"
# Example 2:

# Input: target = "code"
# Output: "RR!DDRR!UUL!R!"
 

# Constraints:

# 1 <= target.length <= 100
# target consists only of English lowercase letters.

def alphabetBoardPath(self, target: str) -> str:
        
    board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
    alphabet_to_position = {}
    
    for ir, row in enumerate(board):
        for ic, word in enumerate(row):
            alphabet_to_position[word] = (ir, ic)
            
    current, path = 'a', ''
    target = list(target)[::-1]
    
    while target:
        curr_pos = alphabet_to_position[current]
        target_pos = alphabet_to_position[target[-1]]
        if curr_pos == target_pos:
            path += '!'
            target.pop()
        elif current == 'z':
            path += 'U'
            current = 'u'
        elif curr_pos[1] > target_pos[1]:
            path += 'L'
            current = board[curr_pos[0]][curr_pos[1] - 1]
        elif curr_pos[1] < target_pos[1]:
            path += 'R'
            current = board[curr_pos[0]][curr_pos[1] + 1]
        elif curr_pos[0] > target_pos[0]:
            path += 'U'
            current = board[curr_pos[0] - 1][curr_pos[1]]
        elif curr_pos[0] < target_pos[0]:
            path += 'D'
            current = board[curr_pos[0] + 1][curr_pos[1]]
            
    return path