# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# Note:

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

def rotate(matrix):

    length = len(matrix)
    dim =  length // 2

    for i in range(dim):
        for t in range(i, length - i - 1):

            temp = matrix[i][t]
            temp1 = matrix[t][length - i - 1]

            matrix[t][length - i - 1] = temp
            temp = matrix[length - i - 1][length - t - 1]

            matrix[length - i - 1][length - t - 1] = temp1
            temp1 = matrix[length - t - 1][i]

            matrix[length - t - 1][i] = temp
            matrix[i][t] = temp1
