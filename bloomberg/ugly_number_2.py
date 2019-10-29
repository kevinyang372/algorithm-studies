# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

# Example:

# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note:  

# 1 is typically treated as an ugly number.
# n does not exceed 1690.

def nthUglyNumber(self, n):
    visited = set([1])
    stack = [1]
    count = 1
    
    while count < n:
        node = heapq.heappop(stack)
        count += 1
        for i in [2,3,5]:
            if node * i not in visited:
                heapq.heappush(stack, node * i)
                visited.add(node * i)
                
    return heapq.heappop(stack)