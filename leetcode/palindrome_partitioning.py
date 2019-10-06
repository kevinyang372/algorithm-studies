# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return all possible palindrome partitioning of s.

# Example:

# Input: "aab"
# Output:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]


## MUCH BETTER WAY TO CHECK PALINDROME

def ispalin(s):
    return s == s[::-1]

# backtracking

def partition(s):
    res = []
    dfs(s, [], res)
    return res

def dfs(s, path, res):
    if s == '':
        res.append(path)
        return

    for i in range(1, len(s) + 1):
        if ispalin(s[:i]):
            dfs(s[i:], path + [s[:i]], res)


# original solution

def partition(s):

    if len(s) < 2: return [[s]]

    res = []
    if ispalindrome(s):
        res.append([s])

    for i in partition(s[1:]):
        temp = sorted([s[0]] + i)
        if temp not in res:
            res.append(temp)
        
    for i in partition(s[:-1]):
        temp = sorted([s[-1]] + i)
        if temp not in res:
            res.append(temp)
            
    return res


def ispalindrome(s):

    i = 0
    j = len(s) - 1

    while j > i:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True