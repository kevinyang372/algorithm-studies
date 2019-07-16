# Given a matrix containing initial state of each elements, find minimum number of steps to reach from top left to bottom right?

# Conditions:

# Initial state of each element will be one of North, East, South or West
# At every step, we can either not move anywhere or move in the direction of current state of that element (ofcourse we never go out of the matrix)
# Any step will simulatanously change the state of all elements of the matrix. States change in a clockwise cyclic manner i.e from N -> E -> S -> W
# I tried solving it the BFS way, but interviewer was not fully satisified with the solution. Any better approaches?

def findShortest(mat):

    d = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
    mat = [[d[t] for t in m] for m in mat]

    stack = [[0, 0, 0]]

    while stack:
        x, y, r = stack.pop(0)
        temp = nextNode(mat, x, y, r)

        if temp == [len(mat) - 1, len(mat[0]) - 1]:
            return r + 1
        
        if temp:
            stack.append(temp + [r + 1])

        stack.append([x, y, r + 1])

    return False


def nextNode(mat, x, y, r):

    if x < 0 or y < 0 or x > len(mat) - 1 or y > len(mat[0]) - 1:
        return False

    d = (mat[x][y] + r) % 4

    if d == 0:
        return [x - 1, y]
    elif d == 1:
        return [x, y + 1]
    elif d == 2:
        return [x + 1, y]
    else:
        return [x, y - 1]