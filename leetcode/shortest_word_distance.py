# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Input: word1 = “coding”, word2 = “practice”
# Output: 3
# Input: word1 = "makes", word2 = "coding"
# Output: 1
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

def shortestDistance(self, words, word1, word2):
    i = j = float('inf')
    min_d = float('inf')
    
    for ind, word in enumerate(words):
        if word1 == word:
            i = ind
        if word2 == word:
            j = ind
        
        min_d = min(min_d, abs(i - j))
    
    return min_d