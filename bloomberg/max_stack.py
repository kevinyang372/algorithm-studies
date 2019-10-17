# Design a max stack that supports push, pop, top, peekMax and popMax.

# push(x) -- Push element x onto stack.
# pop() -- Remove the element on top of the stack and return it.
# top() -- Get the element on the top.
# peekMax() -- Retrieve the maximum element in the stack.
# popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
# Example 1:
# MaxStack stack = new MaxStack();
# stack.push(5); 
# stack.push(1);
# stack.push(5);
# stack.top(); -> 5
# stack.popMax(); -> 5
# stack.top(); -> 1
# stack.peekMax(); -> 5
# stack.pop(); -> 1
# stack.top(); -> 5
# Note:
# -1e7 <= x <= 1e7
# Number of operations won't exceed 10000.
# The last four operations won't be called when stack is empty.

class MaxStack(object):    
    
    def __init__(self):
        self.stack = []
        self.cache = []

    def push(self, x):
        self.stack.append(x)
        if not self.cache or self.cache[-1] < x:
            self.cache.append(x)
        else:
            self.cache.append(self.cache[-1])

    def pop(self):
        self.cache.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]
    
    def peekMax(self):
        return self.cache[-1]
        
    def popMax(self):
        max_val = self.cache[-1]
        temp = []
        while self.stack and self.stack[-1] != max_val:
            temp.append(self.stack.pop())
            self.cache.pop()
        
        self.stack.pop()
        self.cache.pop()
        
        for i in range(len(temp) - 1, -1, -1):
            self.push(temp[i])
        
        return max_val