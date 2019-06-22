# Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks. push () and SetOfStacks. pop () should behave identically to a single stack (that is, pop ( ) should return the same values as it would if there were just a single stack).
# FOLLOW UP
# ImplementafunctionpopAt(int index)whichperformsapopoperationonaspecificsub-stack. Hints: #64, #87

class SetOfStacks:

    def __init__(self, capacity):
        self.current_set = 0
        self.size = 0
        self.stack = [0] * capacity
        self.overall = []

    def isEmpty(self):
        return self.current_set == 0 and self.size == 0

    def push(self, x):
        if self.size == capacity - 1:
            self.overall.append(self.stack)
            self.stack = [0] * capacity
            self.size = 0
            self.stack[self.size] = x
            self.current_set += 1
            self.size += 1
        else:
            self.stack[self.size] = x
            self.size += 1

    def pop(self):
        if self.isEmpty(): raise Exception('Stack is Empty')

        if self.size == 0:
            temp = self.stack[self.size]
            self.stack = [0] * capacity

            if self.current_set > 0: 
                self.overall.pop()
                self.current_set -= 1
                self.size = capacity - 1
        else:
            self.stack[self.size] = 0
            self.size -= 1

    def peek(self):
        if self.isEmpty(): raise Exception('Stack is Empty')
        return self.stack[self.size - 1]



