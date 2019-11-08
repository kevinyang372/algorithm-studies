# A queue can be implemented using an array and two additional fields, the beginning and the end indices. This structure is sometimes referred to as a circular queue. Both enqueue and dequeue have O(1) time complexity.

# Implement a queue API using an array for storing elements. Your API should include a constructor function, which takes as argument the initial capacity of the queue, enqueue and dequeue functions, and a function which returns the number of elements stored. Implement dynamic resizing to support storing an arbitrary large number of elements.

class circularQueue:

    def __init__(self, capacity):
        self._entries = [None] * capacity
        self._num_entries = self._head = self._tail = 0
        self.SCALE_FACTOR = 2

    def enqueue(self, val):
        if self._num_entries == len(self._entries):
            self._entries = self._entries[self._head:] + self._entries[:self._head]
            self._head, self.tail = 0, len(self._entries)
            self._entries += [None] * (len(self._entries) * (self.SCALE_FACTOR - 1))

        self._entries[self._tail] = val
        self._tail = (self._tail + 1) % len(self._entries)
        self._num_entries += 1

    def dequeue(self):
        if not self._num_entries:
            return "No Element in the Queue"

        res = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
        self._num_entries -= 1
        return res

    def size(self):
        return self._num_entries
