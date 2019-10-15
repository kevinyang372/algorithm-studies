# Given an integer array A, and an integer target, return the number of tuples i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target.

# As the answer can be very large, return it modulo 10^9 + 7.

 

# Example 1:

# Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
# Output: 20
# Explanation: 
# Enumerating by the values (A[i], A[j], A[k]):
# (1, 2, 5) occurs 8 times;
# (1, 3, 4) occurs 8 times;
# (2, 2, 4) occurs 2 times;
# (2, 3, 3) occurs 2 times.
# Example 2:

# Input: A = [1,1,2,2,2,2], target = 5
# Output: 12
# Explanation: 
# A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
# We choose one 1 from [1,1] in 2 ways,
# and two 2s from [2,2,2,2] in 6 ways.
 

# Note:

# 3 <= A.length <= 3000
# 0 <= A[i] <= 100
# 0 <= target <= 300

# TLE
def threeSumMulti(self, A, target):
    if len(A) < 3: return 0
    
    count = 0
    A.sort()
    
    for i in range(2, len(A)):
        if A[i] > target: break
        j, r = 0, i - 1
        
        while j < r:
            if A[j] == A[r]:
                if A[i] + A[j] + A[r] == target:
                    count += (r - j + 1) * (r - j) / 2
                break
            if A[i] + A[j] + A[r] == target:
                t = [1, 1]
                while A[j] == A[j + 1]:
                    j += 1
                    t[0] += 1
                
                while A[r] == A[r - 1]:
                    r -= 1
                    t[1] += 1
                
                count += t[0] * t[1]
                j += 1
                r -= 1
            elif A[i] + A[j] + A[r] < target:
                j += 1
            else:
                r -= 1
                
    return count % (10 ** 9 + 7)