# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# The cache is initialized with a positive capacity.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

import heapq
import collections

class LRUCache(object):

    def __init__(self, capacity):
        self.cap = capacity
        self.current = 0
        self.d = collections.defaultdict(int)
        self.age = []
        self.maxage = 0

    def get(self, key):
        
        if key not in self.d:
            return -1
        else:
            for k, v in enumerate(self.age):
                if v[1] == key:
                    self.age[k][0] = self.maxage
                    self.maxage += 1
                    break

            heapq.heapify(self.age)
            return self.d[key]

    def put(self, key, value):
        
        if key in self.d:
            self.d[key] = value
            for k, v in enumerate(self.age):
                if v[1] == key:
                    self.age[k][0] = self.maxage
                    self.maxage += 1
                    break
            heapq.heapify(self.age)  
        elif self.current < self.cap:
            self.d[key] = value
            heapq.heappush(self.age, [self.maxage, key])
            self.maxage += 1
            self.current += 1
        else:
            a, b = heapq.heappushpop(self.age, [self.maxage, key])
            self.d.pop(b)
            self.d[key] = value
            self.maxage += 1

# OrderDict

def __init__(self, capacity):
    self.dic = collections.OrderedDict()
    self.remain = capacity

def get(self, key):
    if key not in self.dic:
        return -1
    v = self.dic.pop(key) 
    self.dic[key] = v   # set key as the newest one
    return v

def put(self, key, value):
    if key in self.dic:    
        self.dic.pop(key)
    else:
        if self.remain > 0:
            self.remain -= 1  
        else:  # self.dic is full
            self.dic.popitem(last=False) 
    self.dic[key] = value

# doubly linked list
class LRUCache(object):
    
    class Node(object):
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity):
        self.cap = capacity
        self.d = {}
        self.head = self.Node('head', 'head')
        self.tail = self.Node('tail', 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.d:
            return -1
        self.insertatfront(self.unlinknode(self.d[key]))
        return self.d[key].val

    def put(self, key, value):
        if key in self.d:
            self.d[key].val = value
            self.insertatfront(self.unlinknode(self.d[key]))
        else:
            if len(self.d) >= self.cap:
                del self.d[self.unlinknode(self.tail.prev).key]
            self.d[key] = self.Node(key, value)
            self.insertatfront(self.d[key])
    
    def unlinknode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
        node.next = None
        node.prev = None
        
        return node
    
    def insertatfront(self, node):
        node.next, self.head.next = self.head.next, node
        node.prev, node.next.prev = self.head, node