# We are given a matrix with R rows and C columns has cells with integer coordinates (r, c), where 0 <= r < R and 0 <= c < C.

# Additionally, we are given a cell in that matrix with coordinates (r0, c0).

# Return the coordinates of all cells in the matrix, sorted by their distance from (r0, c0) from smallest distance to largest distance.  Here, the distance between two cells (r1, c1) and (r2, c2) is the Manhattan distance, |r1 - r2| + |c1 - c2|.  (You may return the answer in any order that satisfies this condition.)

 

# Example 1:

# Input: R = 1, C = 2, r0 = 0, c0 = 0
# Output: [[0,0],[0,1]]
# Explanation: The distances from (r0, c0) to other cells are: [0,1]
# Example 2:

# Input: R = 2, C = 2, r0 = 0, c0 = 1
# Output: [[0,1],[0,0],[1,1],[1,0]]
# Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2]
# The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.
# Example 3:

# Input: R = 2, C = 3, r0 = 1, c0 = 2
# Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
# Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2,2,3]
# There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].

def allCellsDistOrder(R: int, C: int, r0: int, c0: int):

    root = [r0, c0]
    stack = [root]
    result = [root]

    while True:
        node = stack.pop(0)
        new_nodes = []
        
        new_nodes.append([node[0], node[1] - 1])
        new_nodes.append([node[0], node[1] + 1])
        new_nodes.append([node[0] + 1, node[1]])
        new_nodes.append([node[0] - 1, node[1]])

        for i in new_nodes:
            if i not in result and i[0] >= 0 and i[0] < R and i[1] >= 0 and i[1] < C:
                result.append(i)
                stack.append(i)

        if len(stack) == 0:
            break

    return result

