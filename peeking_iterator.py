# Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

# Example:

# Assume that the iterator is initialized to the beginning of the list: [1,2,3].

# Call next() gets you 1, the first element in the list.
# Now you call peek() and it returns 2, the next element. Calling next() after that still return 2. 
# You call next() the final time and it returns 3, the last element. 
# Calling hasNext() after that should return false.
# Follow up: How would you extend your design to be generic and work with all types, not just integer?

# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """

#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """

#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        self.iter = iterator
        self.waiting = []

    def peek(self):
        if self.waiting:
            return self.waiting[0]
        else:
            temp = self.iter.next()
            self.waiting.append(temp)
            return temp

    def next(self):
        if self.waiting:
            return self.waiting.pop(0)
        elif self.hasNext():
            return self.iter.next()

    def hasNext(self):
        if self.iter.hasNext() or self.waiting:
            return True
        return False
