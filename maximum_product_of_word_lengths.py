# Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

# Example 1:

# Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16 
# Explanation: The two words can be "abcw", "xtfn".
# Example 2:

# Input: ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4 
# Explanation: The two words can be "ab", "cd".
# Example 3:

# Input: ["a","aa","aaa","aaaa"]
# Output: 0 
# Explanation: No such pair of words.

# simple hashset
def maxProduct(self, words):
        
    past = []
    max_length = 0
    
    for i, v in enumerate(words):
        temp = set(v)
        for ex, length in past[:i]:
            if len(ex.intersection(temp)) == 0:
                max_length = max(len(v) * length, max_length)
        past.append((temp, len(v)))
    
    return max_length