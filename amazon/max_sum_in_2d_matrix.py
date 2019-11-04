# You are given a 2d matrix and int (maxSum). You need to return the size of maximum square possible in this 2d array whose sum of all elements is less than equal to maxSum.

# Eg:

# input array:
# 1 2 3 4 5
# 8 9 9 9 7
# 6 1 2 1 8
# 1 1 1 1 9
# 9 1 1 1 20

# input maxSum = 10

# output = 3.
# Explaination; following 3*3 suare matrix has sum <= 10
# 1 2 1
# 1 1 1
# 1 1 1

def maxSum(matrix, sums):

	maxlength = 1
	i = j = 0

	while i + maxlength <= len(matrix):
		while i + maxlength <= len(matrix) and j + maxlength <= len(matrix[0]):
			temp = 0
			for t in range(i, i + maxlength): 
				for p in range(j, j + maxlength):
					temp += matrix[t][p]

			if temp > sums:
				j += 1
			else:
				maxlength += 1
		i += 1
		j = 0

	return maxlength - 1