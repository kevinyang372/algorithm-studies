# Implement a MyQueue class which implements a queue using two stacks.

class MyQueue:

    def __init__(self):
        self.inpush = self.MyStack()
        self.inpop = self.MyStack()

    def isEmpty(self):
        return self.inpush.isEmpty() and self.inpop.isEmpty()

    def push(self, x):
        if self.inpop.isEmpty():
            self.inpush.push(x)
        else:
            while not self.inpop.isEmpty():
                self.inpush.push(self.inpop.pop())

    def pop(self):
        if self.isEmpty(): raise Exception('Queue is Empty')

        if self.inpop.isEmpty():
            while not self.inpush.isEmpty():
                self.inpop.push(self.inpush.pop())
            
        return self.inpop.pop()
