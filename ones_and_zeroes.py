# In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

# For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

# Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

# Note:

# The given numbers of 0s and 1s will both not exceed 100
# The size of given string array won't exceed 600.
 

# Example 1:

# Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
# Output: 4

# Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”
 

# Example 2:

# Input: Array = {"10", "0", "1"}, m = 1, n = 1
# Output: 2

# Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".

def findMaxForm(self, strs, m, n):
        
    tar = []
    
    for i in strs:
        t0, t1 = i.count('0'), i.count('1')
        if t0 <= m and t1 <= n:
            tar.append((t0, t1))
    
    if not tar: return 0
    
    res = [[[0] * (n + 1) for _ in range(m + 1)] for _ in tar]
    
    for i, (x, y) in enumerate(tar):
        for m1 in range(m + 1):
            if m1 < x:
                if i == 0: 
                    continue
                else:
                    res[i][m1] = res[i - 1][m1]
                    continue
            for n1 in range(n + 1):
                if n1 < y:
                    if i == 0:
                        continue
                    else:
                        res[i][m1][n1] = res[i - 1][m1][n1]
                else:
                    if i == 0:
                        res[i][m1][n1] = 1
                    else:
                        res[i][m1][n1] = max(res[i - 1][m1 - x][n1 - y] + 1, res[i - 1][m1][n1])
    
    return res[-1][-1][-1]