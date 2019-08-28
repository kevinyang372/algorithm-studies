# Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LFUCache cache = new LFUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.get(3);       // returns 3.
# cache.put(4, 4);    // evicts key 1.
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

# Using ordereddict
class Node:
    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.count = count

class LFUCache(object):

    def __init__(self, capacity):
        self.cap = capacity
        self.key2node = {}
        self.count2node = collections.defaultdict(collections.OrderedDict)
        self.mincount = None
        

    def get(self, key):
        if key not in self.key2node:
            return -1
        
        node = self.key2node[key]
        del self.count2node[node.count][key]
        
        if not self.count2node[node.count]:
            del self.count2node[node.count]
            
        node.count += 1
        self.count2node[node.count][key] = node
        
        if not self.count2node[self.mincount]:
            self.mincount += 1
        
        return node.val
        

    def put(self, key, value):
        if not self.cap:
            return
        
        if key in self.key2node:
            self.key2node[key].val = value
            self.get(key)
            return
        
        if len(self.key2node) == self.cap:
            to_remove, n = self.count2node[self.mincount].popitem(last=False)
            del self.key2node[to_remove]
        
        self.mincount = 1
        self.key2node[key] = self.count2node[1][key] = Node(key, value, 1)
        return