# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Example:

# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3

# deque
class MovingAverage(object):

    def __init__(self, size):
        self.sums = 0
        self.count = collections.deque()
        self.cap = size
        

    def next(self, val):
        if len(self.count) == self.cap:
            self.sums -= self.count.popleft()
        
        self.sums += val
        self.count.append(val)
        return float(self.sums) / len(self.count)
