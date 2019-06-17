# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note:

# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:

# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false

def wordBreak(s, wordDict):

    if len(s) == 0: return False

    for i in range(len(s)):
        if s[:i+1] in wordDict:
            if i == len(s) - 1:
                return True
            if wordBreak(s[i+1:], wordDict):
                return True

    return False

def wordBreak(s, wordDict):

    if len(s) == 0: return False

    mi = len(min(wordDict, key=len))
    ma = len(max(wordDict, key=len))

    dic = [[0] * len(wordDict) for _ in range(len(wordDict))]

    for m in range(len(wordDict)):
        for n in range(m, -1, -1):
            if m - n < mi:
                dic[m][n] = 0
            elif m - n < ma and s[m : n + 1] in wordDict:
                dic[m][n] = 1
                continue
            else:
                for t in range(n - mi, mi - 2, -1):
                    if dic[m][t] in wordDict and dic[t][0] == 1:
                        dic[m][n] = 1
                        break

    return dic[0][len(wordDict) - 1] == 1