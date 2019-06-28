# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

# For example,
# [2,3,4], the median is 3

# [2,3], the median is (2 + 3) / 2 = 2.5

# Design a data structure that supports the following two operations:

# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
 

# Example:

# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
 

# Follow up:

# If all integer numbers from the stream are between 0 and 100, how would you optimize it?
# If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it

import heapq

class MedianFinder(object):

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        
    def addNum(self, num):

        cur_min = self.min_heap[0] if self.min_heap else -float('inf')
        cur_max = -self.max_heap[0] if self.max_heap else float('inf')
            
        if num > cur_min:
            if len(self.min_heap) > len(self.max_heap):
                heapq.heappush(self.max_heap, -cur_min)
                heapq.heappushpop(self.min_heap, num)
            else:
                heapq.heappush(self.min_heap, num)
        else:
            if len(self.max_heap) > len(self.min_heap):
                if num >= cur_max:
                    heapq.heappush(self.min_heap, num)
                else:
                    heapq.heappush(self.min_heap, cur_max)
                    heapq.heappushpop(self.max_heap, -num)
            else:
                heapq.heappush(self.max_heap, -num)

    def findMedian(self):
        
        if len(self.min_heap) == len(self.max_heap):
            return float(self.min_heap[0] - self.max_heap[0]) / 2
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return -self.max_heap[0]
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()