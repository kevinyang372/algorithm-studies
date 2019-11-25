# if a given number has a square root or not.

def hasSquareRoot(num):
	if num < 1: return False

	lower, upper = 1, num
	while lower < upper:
		mid = (lower + upper) // 2
		squared = mid * mid

		if squared == num:
			return True
		elif squared < num:
			lower = mid + 1
		else:
			upper = mid

	return False