# Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters. 

# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Input: word1 = “coding”, word2 = “practice”
# Output: 3
# Input: word1 = "makes", word2 = "coding"
# Output: 1
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

class WordDistance(object):

    def __init__(self, words):
        self.d = collections.defaultdict(list)
        for i, v in enumerate(words):
            self.d[v].append(i)
        

    def shortest(self, word1, word2):
        t1, t2 = self.d[word1], self.d[word2]
        
        i = j = 0
        min_d = float('inf')
        while i < len(t1) and j < len(t2):
            min_d = min(min_d, abs(t1[i] - t2[j]))
            
            if t1[i] < t2[j]:
                i += 1
            else:
                j += 1
        return min_d