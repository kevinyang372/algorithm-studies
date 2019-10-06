# Design a data structure that supports the following two operations:

# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

# Example:

# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.next = []
        self.terminate = False

class WordDictionary(object):

    def __init__(self):
        self.root = TreeNode('')
        
    def addWord(self, word):
        node = self.root
        for k, i in enumerate(word):
            found = False
            for t in node.next:
                if t.val == i:
                    node = t
                    found = True

            if not found:
                temp = TreeNode(i)
                node.next.append(temp)
                node = temp

            if k == len(word) - 1:
                node.terminate = True

    def search(self, word):

        if not word: return True

        stack = [self.root]
        while word:

            cur = word[0]
            word = word[1:]

            if cur == '.':
                temp = []
                for i in stack:
                    temp += i.next
                stack = temp
            else:
                temp = []
                for i in stack:
                    for m in i.next:
                        if m.val == cur:
                            temp.append(m)
                stack = temp

            if not stack:
                return False

        for i in stack:
            if i.terminate:
                return True

        return False