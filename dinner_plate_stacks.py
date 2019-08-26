# You have an infinite number of stacks arranged in a row and numbered (left to right) from 0, each of the stacks has the same maximum capacity.

# Implement the DinnerPlates class:

# DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks.
# void push(int val) pushes the given positive integer val into the leftmost stack with size less than capacity.
# int pop() returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns -1 if all stacks are empty.
# int popAtStack(int index) returns the value at the top of the stack with the given index and removes it from that stack, and returns -1 if the stack with that given index is empty.
# Example:

# Input: 
# ["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
# [[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
# Output: 
# [null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]

# Explanation: 
# DinnerPlates D = DinnerPlates(2);  // Initialize with capacity = 2
# D.push(1);
# D.push(2);
# D.push(3);
# D.push(4);
# D.push(5);         // The stacks are now:  2  4
#                                            1  3  5
#                                            ﹈ ﹈ ﹈
# D.popAtStack(0);   // Returns 2.  The stacks are now:     4
#                                                        1  3  5
#                                                        ﹈ ﹈ ﹈
# D.push(20);        // The stacks are now: 20  4
#                                            1  3  5
#                                            ﹈ ﹈ ﹈
# D.push(21);        // The stacks are now: 20  4 21
#                                            1  3  5
#                                            ﹈ ﹈ ﹈
# D.popAtStack(0);   // Returns 20.  The stacks are now:     4 21
#                                                         1  3  5
#                                                         ﹈ ﹈ ﹈
# D.popAtStack(2);   // Returns 21.  The stacks are now:     4
#                                                         1  3  5
#                                                         ﹈ ﹈ ﹈ 
# D.pop()            // Returns 5.  The stacks are now:      4
#                                                         1  3 
#                                                         ﹈ ﹈  
# D.pop()            // Returns 4.  The stacks are now:   1  3 
#                                                         ﹈ ﹈   
# D.pop()            // Returns 3.  The stacks are now:   1 
#                                                         ﹈   
# D.pop()            // Returns 1.  There are no stacks.
# D.pop()            // Returns -1.  There are still no stacks.
 

# Constraints:

# 1 <= capacity <= 20000
# 1 <= val <= 20000
# 0 <= index <= 100000
# At most 200000 calls will be made to push, pop, and popAtStack.

# using heap
class DinnerPlates(object):

    def __init__(self, capacity):
        self.cap = capacity
        self.hascapacity = [0]
        self.withplates = set()
        self.max = 1
        self.stack = collections.defaultdict(list)
        

    def push(self, val):
        self.stack[self.hascapacity[0]].append(val)
        self.withplates.add(self.hascapacity[0])
        
        if len(self.stack[self.hascapacity[0]]) == self.cap:
            if len(self.hascapacity) == 1:
                heapq.heappushpop(self.hascapacity, self.max)
                self.max += 1
            else:
                heapq.heappop(self.hascapacity)

                
    def pop(self):
        if len(self.withplates) == 0:
            return -1
        
        t = max(self.withplates)
        
        if len(self.stack[t]) == self.cap:
            heapq.heappush(self.hascapacity, t)
        elif len(self.stack[t]) == 1:
            self.withplates.remove(t)
            
        return self.stack[t].pop()

    def popAtStack(self, index):
        if len(self.stack[index]) == self.cap:
            heapq.heappush(self.hascapacity, index)
            return self.stack[index].pop()
        elif len(self.stack[index]) > 1:
            return self.stack[index].pop()
        elif len(self.stack[index]) == 1:
            self.withplates.remove(index)
            return self.stack[index].pop()
        else:
            return -1

# using stack
class DinnerPlates:

    def __init__(self, capacity):
        self.queue = []
        self.c = capacity
        self.emp = []

    def push(self, val):
        if self.emp:
            l = heapq.heappop(self.emp)
            if l < len(self.queue):
                self.queue[l] += [val]
                return
            else: self.emp = []
        if len(self.queue)>0 and len(self.queue[-1]) < self.c:
            self.queue[-1] += [val]
            return
        self.queue += [[val]]

    def pop(self):
        while len(self.queue) > 0 and not self.queue[-1]:
            self.queue.pop()
        if self.queue:
            res = self.queue[-1][-1]
            self.queue[-1].pop()
            return res
        return -1

    def popAtStack(self, index):
        if index < len(self.queue) and len(self.queue[index]) > 0:
            res = self.queue[index][-1]
            self.queue[index].pop()
            heapq.heappush(self.emp,index)
            return res
        return -1