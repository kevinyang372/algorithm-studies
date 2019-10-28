# Design a data structure that support the following methods:

# public class Stream {
    
#     public Stream() {
#         // do intialization if necessary
#     }

# 	/**
# 	* Adds integer num to a stream of integers.
# 	*/
#     public void add(int num) {
#         // write your code here
#     }

# 	/**
# 	*  Returns the first unique integer in the stream if found else return null.
# 	*/
#     public Integer getFirstUnique() {
#         // write your code here
#     }
# }
# Example:

# Stream s = new Stream();
# s.add(2);
# s.getFirstUnique(); // 2
# s.add(2);
# s.getFirstUnique(); // null
# s.add(3);
# s.getFirstUnique(); // 3
# s.add(4);
# s.getFirstUnique(); // 3
# s.add(3);
# s.getFirstUnique(); // 4

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class Stream(object):

    def __init__(self):
        self.visited = set()
        self.d = {}
        self.HEAD = Node('HEAD')
        self.TAIL = Node('TAIL')

        self.HEAD.next = self.TAIL
        self.TAIL.prev = self.HEAD

    def unlinkNode(self, node):
        pre, ne = node.prev, node.next
        pre.next, ne.prev = ne, pre

    def insertAtTail(self, node):
        pre = self.TAIL.prev
        pre.next, self.TAIL.prev = node, node
        node.prev = pre
        node.next = self.TAIL

    def add(self, val):
        if val not in self.visited:
            if val in self.d:
                node = self.d[val]
                del self.d[val]
                self.unlinkNode(node)
                self.visited.add(val)
            elif val not in self.d:
                node = Node(val)
                self.insertAtTail(node)
                self.d[val] = node

    def getFirstUnique(self):
        if self.HEAD.next != self.TAIL:
            return self.HEAD.next.val
        return None