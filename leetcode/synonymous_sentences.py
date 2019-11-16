# Given a list of pairs of equivalent words synonyms and a sentence text, Return all possible synonymous sentences sorted lexicographically.
 

# Example 1:

# Input:
# synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],
# text = "I am happy today but was sad yesterday"
# Output:
# ["I am cheerful today but was sad yesterday",
# ​​​​​​​"I am cheerful today but was sorrow yesterday",
# "I am happy today but was sad yesterday",
# "I am happy today but was sorrow yesterday",
# "I am joy today but was sad yesterday",
# "I am joy today but was sorrow yesterday"]
 

# Constraints:

# 0 <= synonyms.length <= 10
# synonyms[i].length == 2
# synonyms[0] != synonyms[1]
# All words consist of at most 10 English letters only.
# text is a single space separated sentence of at most 10 words.

class DSU:
    def __init__(self, words, maps):
        self.p = [i for i in range(len(words))]
        self.p2w = {v:i for i, v in enumerate(words)}
        self.w2p = {i:v for i, v in enumerate(words)}
        self.maps = maps
        
    def find(self, y):
        if y != self.p[y]:
            self.p[y] = self.find(self.p[y])
        return self.p[y]
    
    def union(self, x, y):
        if x in self.maps or self.p[self.p2w[x]] != self.p2w[x]:
            self.p[self.find(self.p2w[y])] = self.p[self.p2w[x]]
        else:
            self.p[self.find(self.p2w[x])] = self.p[self.p2w[y]]
    
    def result(self):
        res = collections.defaultdict(list)
        sameMeaning = {}
        for i, v in enumerate(self.p):
            if self.w2p[i] in self.maps and i != v:
                sameMeaning[self.w2p[i]] = self.w2p[v]
            res[self.w2p[v]].append(self.w2p[i])
        
        for i in sameMeaning:
            res[i] = res[sameMeaning[i]]
            
        return res
    
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        
        maps = set(text.split(' '))
        graph = collections.defaultdict(list)
        words = set()
        
        for x, y in synonyms:
            words.add(x)
            words.add(y)
        
        dsu = DSU(words, maps)
        for x, y in synonyms:
            dsu.union(x, y)
        
        graph = dsu.result()
                
        def dfs(t):
            if not t: return [[]]
            
            prev = []
            for i, v in enumerate(t):
                if v not in graph:
                    prev.append(v)
                else:
                    temp = dfs(t[i + 1:])
                    to_con = sorted(graph[v])
                    
                    return [prev + [m] + p for m in to_con for p in temp]
            
            return [prev]
        
        return [' '.join(p) for p in dfs(text.split(' '))]