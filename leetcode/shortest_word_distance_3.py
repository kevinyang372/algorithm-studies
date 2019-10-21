# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

# word1 and word2 may be the same and they represent two individual words in the list.

# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Input: word1 = “makes”, word2 = “coding”
# Output: 1
# Input: word1 = "makes", word2 = "makes"
# Output: 3
# Note:
# You may assume word1 and word2 are both in the list.

def shortestWordDistance(self, words, word1, word2):
        
    if word1 == word2:
        i = j = None
        min_d = float('inf')
        
        for ind, val in enumerate(words):
            if val == word1:
                if i is None:
                    i = ind
                elif j is None or j < i:
                    j = ind
                    min_d = min(min_d, abs(j - i))
                else:
                    i = ind
                    min_d = min(min_d, abs(j - i))
        return min_d
    else:
        i = j = float('inf')
        min_d = float('inf')

        for ind, word in enumerate(words):
            if word1 == word:
                i = ind
            if word2 == word:
                j = ind

            min_d = min(min_d, abs(i - j))

        return min_d
