# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# Example 1:

# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:

# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"

# dynamic programming O(N^2) MLE
def longestValidParentheses(self, s: str) -> int:
        
    dp = [[0] * len(s) for _ in range(len(s))]
    max_val = 0
    
    for i in range(len(s)):
        if s[i] == "(":
            dp[i][i] = 1
            for j in range(i + 1, len(s)):
                if s[j] == "(":
                    dp[i][j] = dp[i][j - 1] + 1
                elif s[j] == ")" and dp[i][j - 1] > 0:
                    dp[i][j] = dp[i][j - 1] - 1
                    if dp[i][j] == 0:
                        max_val = max(max_val, j - i + 1)
                elif s[j] == ")" and dp[i][j - 1] <= 0:
                    break
        else:
            continue
    
    return max_val

# O(N) solution
def longestValidParentheses(self, s: str) -> int:
        
        if not s: return 0
        dp = [0] * len(s)
        
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                elif i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                    dp[i] = dp[i - dp[i-1] - 2] + dp[i-1] + 2
        
        return max(dp)

# for subsequences (not solution for this problem)
def longestValidParentheses(self, s: str) -> int:
    while s and s[0] == ')':
        s = s[1:]
        
    while s and s[-1] == '(':
        s = s[:-1]
        
    def traverse(sums, arr, l):
        if not arr: return 0
        max_val = 0
        if arr[0] == ")":
            sums -= 1
            if sums == 0:
                max_val = max(max_val, l + 1)
            elif sums < 0:
                return 0
        elif arr[0] == "(":
            sums += 1
        
        for i in range(1, len(arr)):
            max_val = max(max_val, traverse(sums, arr[i:], l + 1))
            
        return max_val
                
    return traverse(0, list(s), 0)