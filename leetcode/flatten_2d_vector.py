# Design and implement an iterator to flatten a 2d vector. It should support the following operations: next and hasNext.

 

# Example:

# Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

# iterator.next(); // return 1
# iterator.next(); // return 2
# iterator.next(); // return 3
# iterator.hasNext(); // return true
# iterator.hasNext(); // return true
# iterator.next(); // return 4
# iterator.hasNext(); // return false
 

# Notes:

# Please remember to RESET your class variables declared in Vector2D, as static/class variables are persisted across multiple test cases. Please see here for more details.
# You may assume that next() call will always be valid, that is, there will be at least a next element in the 2d vector when next() is called.
 

# Follow up:

# As an added challenge, try to code it using only iterators in C++ or iterators in Java.

class Vector2D(object):

    def __init__(self, v):
        self.arr = [i[::-1] for i in v[::-1] if len(i) > 0]
        

    def next(self):
        res = self.arr[-1].pop()
        if not self.arr[-1]:
            self.arr.pop()
        return res
        

    def hasNext(self):
        return len(self.arr) > 0