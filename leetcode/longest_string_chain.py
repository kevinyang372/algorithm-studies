# Given a list of words, each word consists of English lowercase letters.

# Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

# Return the longest possible length of a word chain with words chosen from the given list of words.

 

# Example 1:

# Input: ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: one of the longest word chain is "a","ba","bda","bdca".
 

# Note:

# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of English lowercase letters.

def longestStrChain(self, words: List[str]) -> int:
        
    d = collections.defaultdict(list)
    c = [collections.Counter(word) for word in words]
    
    for i, word in enumerate(words):
        d[len(word)].append([word, c[i]])
    
    cache = collections.Counter()
    minv, maxv = min(d.keys()), max(d.keys())
    res = 0
    
    for i in range(minv, maxv):
        for w1, c1 in d[i]:
            for w2, c2 in d[i + 1]:
                diff = c2 - c1
                if sum([diff[i] for i in diff]) == 1:
                    cache[w2] = max(cache[w1] + 1, cache[w2])
                    res = max(res, cache[w2])
    
    return res + 1