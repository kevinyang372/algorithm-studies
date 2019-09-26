# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

# Example 1:
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:
# Input: 9973
# Output: 9973
# Explanation: No swap.
# Note:
# The given number is in the range [0, 108]

def maximumSwap(self, num):
        
    if num < 10: return num
    
    num = list(str(num))
    num[0] = int(num[0])
    
    res = None
    
    for i in range(len(num)):
        num[i] = int(num[i])
        for j in range(i):
            if num[i] > num[j]:
                if not res or j < res[1] or j == res[1] and num[i] >= num[res[0]]:
                    res = (i, j)
                break
    
    if not res:
        return sum([i * 10 ** (len(num) - t - 1) for t, i in enumerate(num)])
    
    num[res[0]], num[res[1]] = num[res[1]], num[res[0]]
    return sum([i * 10 ** (len(num) - t - 1) for t, i in enumerate(num)])