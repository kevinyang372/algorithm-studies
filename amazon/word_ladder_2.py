# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:

# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:

# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# Output:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
# Example 2:

# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# Output: []

# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

def findLadders(beginWord, endWord, wordList):

    if endWord not in wordList: return

    fin = []    
    min_length = float('inf')
    
    for k, v in enumerate(wordList):
        
        if distance(v, beginWord) == 1:
            if v == endWord:
                return [[beginWord, v]]

            temp = findLadders(v, endWord, wordList[:k] + wordList[k+1:])
            
            for i in temp:
                if len(i) > min_length:
                    continue
                elif len(i) < min_length:
                    fin = [[beginWord] + i]
                    min_length = len(i)
                else:
                    fin.append([beginWord] + i)

    return fin

def distance(w1, w2):

    d = 0

    for k, v in enumerate(w1):
        if w2[k] != v:
            d += 1

    return d