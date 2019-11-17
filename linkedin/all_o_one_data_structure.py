# Implement a data structure supporting the following operations:

# Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
# Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
# GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
# GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
# Challenge: Perform all these in O(1) time complexity.

class Node:
    def __init__(self, q, level):
        self.q = q
        self.level = level
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        self.k2n = {}
        self.head = Node("HEAD", -1)
        self.tail = Node("TAIL", -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def unlinkNode(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
    
    def insertNode(self, node, n1):
        n = n1.next
        node.next, node.prev = n, n1
        n.prev = node
        n1.next = node

    def inc(self, key: str) -> None:
        if key in self.k2n:
            node = self.k2n[key]
            l1 = node.level
            
            if node.next.level != l1 + 1:
                self.insertNode(Node(set(), l1 + 1), node)
            
            node.next.q.add(key)
            node.q.remove(key)
            self.k2n[key] = node.next
            
            if len(node.q) == 0:
                self.unlinkNode(node)
        else:
            if self.head.next.level != 1:
                self.insertNode(Node(set(), 1), self.head)
            self.head.next.q.add(key)
            self.k2n[key] = self.head.next

    def dec(self, key: str) -> None:
        if key not in self.k2n: return
        
        node = self.k2n[key]
        node.q.remove(key)
        
        if node.level == 1:
            self.k2n.pop(key)
        else:
            if node.prev.level != node.level - 1:
                self.insertNode(Node(set(), node.level - 1), node.prev)
                
            node.prev.q.add(key)
            self.k2n[key] = node.prev
        
        if len(node.q) == 0:
            self.unlinkNode(node)

            
    def getMaxKey(self) -> str:
        if self.tail.prev.level == -1: return ""
        return next(iter(self.tail.prev.q))
        

    def getMinKey(self) -> str:
        if self.head.next.level == -1: return ""
        return next(iter(self.head.next.q))