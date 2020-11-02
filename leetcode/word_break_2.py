# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

# Note:

# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:

# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# Example 2:

# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []

def wordBreak(s, wordDict):
        res = [[] for _ in range(len(s) + 1)]
        res[0].append('')

        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in wordDict and res[j]:
                    res[i].append(s[j:i])

        return joinResult(res, len(s), [])
    
def joinResult(res, ind, stack):
    if ind == 0:
        return stack
    
    s = []
    for i in res[ind]:
        if not stack:
            s += joinResult(res, ind - len(i), [i])
        else:
            s += joinResult(res, ind - len(i), ["%s %s" % (i, t) for t in stack])
    return s


def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    if not wordDict: return []
    wordDict = set(wordDict)
    max_len = len(max(wordDict, key=len))
    
    @lru_cache
    def search(ind, prev):
        if len(prev) > max_len: return []
        curr = prev + s[ind]
        res = []
        
        if ind == len(s) - 1:
            if curr in wordDict:
                return [curr]
            else:
                return []
        
        if curr in wordDict:
            res.extend([f"{curr} {i}" for i in search(ind + 1, '')])
        
        res.extend(search(ind + 1, curr))
        return res
    
    return search(0, '')
