# Implement a magic directory with buildDict, and search methods.

# For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

# For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.

# Example 1:
# Input: buildDict(["hello", "leetcode"]), Output: Null
# Input: search("hello"), Output: False
# Input: search("hhllo"), Output: True
# Input: search("hell"), Output: False
# Input: search("leetcoded"), Output: False
# Note:
# You may assume that all the inputs are consist of lowercase letters a-z.
# For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
# Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode("")
        
    def insert(self, word):
        head = self.root
        
        for i in word:
            if i not in head.children:
                head.children[i] = TrieNode(i)
            head = head.children[i]
        
        head.end = True
                

class MagicDictionary(object):

    def __init__(self):
        self.trie = Trie()
        

    def buildDict(self, dict):
        for i in dict:
            self.trie.insert(i)
        

    def search(self, word):
        
        def dfs(node, w, has_one):
            if not w: return has_one and node.end
            if w[0] in node.children and dfs(node.children[w[0]], w[1:], has_one):
                return True
            if not has_one:
                for n in node.children:
                    if n != w[0] and dfs(node.children[n], w[1:], True):
                        return True
            return False
        
        return dfs(self.trie.root, word, False)

# brute-force
class MagicDictionary:

    def __init__(self):
        self.find_difference = lambda x, y: sum(1 for ind in range(len(x)) if x[ind] != y[ind])
        self.d = collections.defaultdict(list)
        

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.d[len(word)].append(word)
        

    def search(self, searchWord: str) -> bool:
        return any(self.find_difference(word, searchWord) == 1 for word in self.d[len(searchWord)])