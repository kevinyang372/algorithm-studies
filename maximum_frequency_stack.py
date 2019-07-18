# Implement FreqStack, a class which simulates the operation of a stack-like data structure.

# FreqStack has two functions:

# push(int x), which pushes an integer x onto the stack.
# pop(), which removes and returns the most frequent element in the stack.
# If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.

# Example 1:

# Input: 
# ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
# [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
# Output: [null,null,null,null,null,null,null,5,7,5,4]
# Explanation:
# After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

# pop() -> returns 5, as 5 is the most frequent.
# The stack becomes [5,7,5,7,4].

# pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
# The stack becomes [5,7,5,4].

# pop() -> returns 5.
# The stack becomes [5,7,4].

# pop() -> returns 4.
# The stack becomes [5,7].
 

# Note:

# Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
# It is guaranteed that FreqStack.pop() won't be called if the stack has zero elements.
# The total number of FreqStack.push calls will not exceed 10000 in a single test case.
# The total number of FreqStack.pop calls will not exceed 10000 in a single test case.
# The total number of FreqStack.push and FreqStack.pop calls will not exceed 150000 across all test cases.

# TLE
class FreqStack(object):

    def __init__(self):
        self.stack = 0
        self.freq = collections.Counter()
        self.order = collections.defaultdict(list)

    def push(self, x):
        self.stack += 1
        self.freq[x] += 1
        self.order[x].append(self.stack)

    def pop(self):
        max_val = []
        max_num = 0
        for i, v in self.freq.items():
            if v > 0:
                if v > max_num:
                    max_num = v
                    max_val = i
                elif v == max_num:
                    max_val = max(i, max_val, key=lambda x: self.order[x][-1])
                
        self.freq[max_val] -= 1
        self.order[max_val].pop()
        
        return max_val

# stack with stack
class FreqStack(object):

    def __init__(self):
        self.maxfreq = 0
        self.freq = collections.Counter()
        self.order = collections.defaultdict(list)

    def push(self, x):
        f = self.freq[x] + 1
        self.freq[x] = f
        
        if f > self.maxfreq:
            self.maxfreq = f
            
        self.order[f].append(x)

    def pop(self):
        val = self.order[self.maxfreq].pop()
        self.freq[val] -= 1
        if not self.order[self.maxfreq]:
            self.maxfreq -= 1
        return val