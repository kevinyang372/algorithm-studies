# Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

# For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

# Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.

# Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

# Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

# Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

# Note:

# The length of words1 and words2 will not exceed 1000.
# The length of pairs will not exceed 2000.
# The length of each pairs[i] will be 2.
# The length of each words[i] and pairs[i][j] will be in the range [1, 20].

class DSU:
    def __init__(self):
        self.q = range(2001)
    
    def find(self, x):
        if self.q[x] != x:
            self.q[x] = self.find(self.q[x])
        return self.q[x]
    
    def union(self, x, y):
        self.q[self.find(x)] = self.find(y)
    

def areSentencesSimilarTwo(self, words1, words2, pairs):
    
    if len(words1) != len(words2): return False
    
    dsu = DSU()
    c = 0
    word2id = {}
    
    for x, y in pairs:
        if x in word2id:
            id1 = word2id[x]
        else:
            id1 = c
            word2id[x] = c
            c += 1
            
        if y in word2id:
            id2 = word2id[y]
        else:
            id2 = c
            word2id[y] = c
            c += 1
            
        dsu.union(id1, id2)
    
    i = 0
    while i < len(words1):
        x1, y1 = words1[i], words2[i]
        if x1 == y1:
            i += 1
            continue
        if x1 not in word2id or y1 not in word2id:
            return False
        if dsu.find(word2id[x1]) != dsu.find(word2id[y1]):
            return False
        i += 1
        
    return True