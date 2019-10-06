# Nearly every one have used the Multiplication Table. But could you find out the k-th smallest number quickly from the multiplication table?

# Given the height m and the length n of a m * n Multiplication Table, and a positive integer k, you need to return the k-th smallest number in this table.

# Example 1:
# Input: m = 3, n = 3, k = 5
# Output: 
# Explanation: 
# The Multiplication Table:
# 1   2   3
# 2   4   6
# 3   6   9

# The 5-th smallest number is 3 (1, 2, 2, 3, 3).
# Example 2:
# Input: m = 2, n = 3, k = 6
# Output: 
# Explanation: 
# The Multiplication Table:
# 1   2   3
# 2   4   6

# The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
# Note:
# The m and n will be in the range [1, 30000].
# The k will be in the range [1, m * n]

# heap TLE
def findKthNumber(self, m, n, k):
        
    start = (1, 1, 1)
    d = [start]
    count = 0
    visited = set()
    
    if m > n:
        m, n = n, m
    
    while count < k:
        node, x, y = heapq.heappop(d)
        
        if x > y:
            x, y = y, x
        
        if (x, y) in visited or x > m or y > n:
            continue
        
        visited.add((x, y))
        heapq.heappush(d, (x * (y + 1), x, y + 1))
        
        if x == y:
            count += 1
        else:
            heapq.heappush(d, ((x + 1) * y, x + 1, y))
            
            if y > m:
                count += 1
            else:
                count += 2
            
    return node

# binary search
def findKthNumber(self, m, n, k):
    def enough(x):
        count = 0
        for i in range(1, m + 1):
            count += min(x // i, n)
        return count >= k
    
    lo, hi = 1, m * n
    while lo < hi:
        mi = (lo + hi) / 2
        if not enough(mi):
            lo = mi + 1
        else:
            hi = mi
    return lo