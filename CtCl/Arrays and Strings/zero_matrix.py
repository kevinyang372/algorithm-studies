# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to O

def zero_matrix(mat):

    row = []
    col = []

    for m in range(len(mat)):
        for n in range(len(mat[0])):
            if mat[m][n] == 0:
                if m not in row:
                    row.append(m)
                if n not in col:
                    col.append(n)

    for i in row:
        mat[i] = [0] * len(mat[0])

    mat = [list(i) for i in zip(*mat[::-1])]

    for i in col:
        mat[i] = [0] * len(mat[0])

    return [list(i) for i in zip(*reversed(mat[::-1]))][::-1]