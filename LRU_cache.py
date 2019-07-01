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