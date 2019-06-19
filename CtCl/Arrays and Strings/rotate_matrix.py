# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. (an you do this in place?

def rotate_matrix(mat):

    for i in range(len(mat) // 2):
        for t in range(i, len(mat) - i - 1):
            mat[i][i + t], mat[i + t][len(mat) - i - 1], mat[len(mat) - i - 1][len(mat) - t - 1], mat[len(mat) - t - 1][i] = mat[len(mat) - t - 1][i], mat[i][i + t], mat[i + t][len(mat) - i - 1], mat[len(mat) - i - 1][len(mat) - t - 1]

    return mat