# Implement a trie with insert, search, and startsWith methods.

# Example:

# Trie trie = new Trie();

# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# Note:

# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.

class Trie(object):

    def __init__(self):
        self.root = TreeNode("")

    def insert(self, word):

        last = self.root
        for i in word:
            temp = False

            for t in last.next:
                if i == t.val:
                    last = t
                    temp = True
                    break

            if not temp:
                new = TreeNode(i)
                last.next.append(new)
                last = new

        last.landed = True
        

    def search(self, word):
        
        last = self.root

        for i in word:
            temp = False

            for t in last.next:
                if i == t.val:
                    last = t
                    temp = True
                    break

            if not temp:
                return False

        if last.landed:
            return True
        
        return False
        

    def startsWith(self, prefix):

        last = self.root

        for i in prefix:
            temp = False

            for t in last.next:
                if i == t.val:
                    last = t
                    temp = True
                    break

            if not temp:
                return False

        return True
        
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.landed = False
        self.next = []


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)