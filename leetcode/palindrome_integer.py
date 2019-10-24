# Given an integer n, find the closest integer (not including itself), which is a palindrome.

# The 'closest' is defined as absolute difference minimized between two integers.

# Example 1:
# Input: "123"
# Output: "121"
# Note:
# The input n is a positive integer represented by string, whose length will not exceed 18.
# If there is a tie, return the smaller one as answer.

def palindromeInteger(i):
    if i < 10: return i
    
    s = str(i)
    if len(s) % 2 == 0:
        x = s[:len(s) // 2]
        temp = []
        for dx in [-1, 0, 1]:
            y = int(x) + dx
            
            if y == 0:
                temp.append(9)
                continue
            else:
                y = str(y)
            
            new_num = y + y[::-1]
            temp.append(int(new_num))    
    else:
        x = s[:len(s) // 2]
        temp = []
        for dx in [-1, 0, 1]:
            y = int(x) + dx
            
            if y == 0:
                temp.append(99)
                continue
            else:
                y = str(y)
                
            for mid in range(0, 10):
                new_num = y + str(mid) + y[::-1]
                temp.append(int(new_num))
                    
    return min(temp, key=lambda x: (abs(x - i), temp))