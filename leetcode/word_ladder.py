# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:

# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:

# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# Output: 5

# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# Example 2:

# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# Output: 0

# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

# mapping TLE
def ladderLength(self, beginWord, endWord, wordList):

    if endWord not in wordList: return 0
    
    def distance(a, b):
        d = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                d += 1
        return d
    
    mapping = collections.defaultdict(list)
    
    for i in range(len(wordList)):
        if distance(beginWord, wordList[i]) == 1:
            mapping[beginWord].append(wordList[i])
        for t in range(i + 1, len(wordList)):
            if distance(wordList[t], wordList[i]) == 1:
                mapping[wordList[i]].append(wordList[t])
                mapping[wordList[t]].append(wordList[i])
    
    seen = set([beginWord])
    queue = [beginWord]
    count = 1
    
    while queue:
        temp = []
        for i in queue:
            for t in mapping[i]:
                if t == endWord:
                    return count + 1
                if t not in seen:
                    temp.append(t)
                    seen.add(t,)

        queue = temp
        count += 1
    
    return 0

# word prep + bfs
import collections

def ladderLength(self, beginWord, endWord, wordList):

    if endWord not in wordList: return 0
    
    mapping = collections.defaultdict(list)
    length = len(beginWord)
    
    for i in wordList:
        for m in range(length):
            masked = i[:m] + '_' + i[m + 1:]
            mapping[masked].append(i)
    
    seen = set([beginWord])
    queue = collections.deque([(beginWord, 1)])
    
    while queue:
        node, count = queue.popleft()
        for i in range(length):
            masked = node[:i] + '_' + node[i + 1:]
            for neigh in mapping[masked]:
                if neigh == endWord:
                    return count + 1
                if neigh not in seen:
                    queue.append([neigh, count + 1])
                    seen.add(neigh,)
    
    return 0