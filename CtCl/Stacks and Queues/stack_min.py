# How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in 0(1) time.

import sys

class min_stack:

    def __init__(self, stacksize):
        self.stacksize = stacksize
        self.stack = [0] * stacksize
        self.size = 0
        self.min = [sys.maxint] * stacksize

    def isFull(self):
        return len(stack) == stacksize

    def isEmpty(self):
        return len(stack) == 0

    def push(self, x):
        if self.isFull(): raise Exception('Stack is Full')
        self.stack[self.size] = x

        if self.isEmpty():
            self.min[self.size] = x
        else:
            self.min[self.size] = min(x, self.min[self.size - 1])

        self.size += 1

    def pop(self):
        if self.isEmpty(): raise Exception('Stack is Empty')

        self.stack[self.size] = 0
        self.size -= 1
        
        return self.stack[self.size + 1]

    def peek(self):
        return self.stack[self.size]

    def min(self):
        return self.min[self.size]

