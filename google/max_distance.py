# The distance between 2 binary strings is the sum of their lengths after removing the common prefix. For example: the common prefix of 1011000 and 1011110 is 1011 so the distance is len("000") + len("110") = 3 + 3 = 6.

# Given a list of binary strings, pick a pair that gives you maximum distance among all possible pair and return that distance.

import collections

class TrieNode:
    def __init__(self):
        self.ch = collections.defaultdict(TrieNode)
        self.end = False
        self.h = 0

    def add(self, s):
        node, n = self, len(s)
        for i, v in enumerate(s):
            node = node.ch[v]
            node.h = max(node.h, n - i)
        node.end = True

    def dist(self, s):
        node, n, cand = self, len(s), []

        for i, v in enumerate(s):
            if node.end: cand.append(n - i)

            mismatch = '1' of v == '0' else '0'
            if mismatch in node.ch: cand.append(n - i + node.ch[mismatch].h)

            if v in node.ch:
                node = node.ch[v]
            else:
                break

        return max(cand)

def maxDistance(self, a, b):

    root.TrieNode()
    for i in a:
        root.add(i)
    return max([root.dist(i) for i in b])