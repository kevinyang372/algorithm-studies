# Question: Can you break the given string into words, provided by a given hashmap of frequency of word as <word: n>

# Example 1:

# HashMap -> {"abc":3, "ab":2, "abca":1}
# String: "abcabcabcabca"
# Output: true
# Explanation: "abc" + "abc" + "abc" + "abca"
# Example 2:

# HashMap -> {"abc":3, "ab":2}
# String: "abcabab"
# Output: true
# Explanation: "abc" + "ab" + "ab"
# Example 3:

# HashMap -> {"abc":3, "ab":2, "abca":1}
# String: "abcx"
# Output: false

# word break backtracking + memoization
def wordBreak(self, s, wordDict):
        
    wordDict = set(wordDict)
    cache = set()
    
    def traverse(sub):
        if sub in wordDict: return True
        if sub in cache: return False
        
        for i in range(1, len(sub)):
            if sub[:i] in wordDict and traverse(sub[i:]):
                return True
        
        cache.add(sub)
        return False
    
    return traverse(s)