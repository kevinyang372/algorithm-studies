# Given a 2D board and a list of words from the dictionary, find all words in the board.

# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

# Example:

# Input: 
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]

# Output: ["eat","oath"]

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode("#")
        
    def insert(self, word):
        start = self.root
        
        for c in word:
            if c not in start.children:
                start.children[c] = TrieNode(c)
            start = start.children[c]
        
        start.end = True
        
    def startWith(self, prefix):
        start = self.root
        
        for c in prefix:
            if c not in start.children:
                return False
            start = start.children[c]

        return start
    
    def has(self, word):
        start = self.startWith(word)
        return start.end

class Solution(object):
    def findWords(self, board, words):
        
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        def dfs(x, y, prefix, word, visited):
            if prefix.end:
                res = [word]
            else:
                res = []
                
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                if 0 <= x + dx < len(board) and 0 <= y + dy < len(board[0]) and board[x + dx][y + dy] in prefix.children and (x + dx, y + dy) not in visited:
                    res += dfs(x + dx, y + dy, prefix.children[board[x + dx][y + dy]], word + board[x + dx][y + dy], visited + [(x + dx, y + dy)])
            return res
                    
        
        fin = []
        for m in range(len(board)):
            for n in range(len(board[0])):
                t = trie.startWith(board[m][n])
                if t:
                    fin += dfs(m, n, t, board[m][n], [(m, n)])
        
        return list(set(fin))