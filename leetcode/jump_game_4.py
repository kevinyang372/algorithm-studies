# Given an array of integers arr, you are initially positioned at the first index of the array.

# In one step you can jump from index i to index:

# i + 1 where: i + 1 < arr.length.
# i - 1 where: i - 1 >= 0.
# j where: arr[i] == arr[j] and i != j.
# Return the minimum number of steps to reach the last index of the array.

# Notice that you can not jump outside of the array at any time.

 

# Example 1:

# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
# Example 2:

# Input: arr = [7]
# Output: 0
# Explanation: Start index is the last index. You don't need to jump.
# Example 3:

# Input: arr = [7,6,9,6,9,6,9,7]
# Output: 1
# Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
# Example 4:

# Input: arr = [6,1,9]
# Output: 2
# Example 5:

# Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
# Output: 3
 

# Constraints:

# 1 <= arr.length <= 5 * 10^4
# -10^8 <= arr[i] <= 10^8

def minJumps(self, arr: List[int]) -> int:
        
    d = collections.defaultdict(list)
    
    for i, v in enumerate(arr):
        if i - 1 >= 0 and i + 1 < len(arr) and v == arr[i - 1] == arr[i + 1]:
            continue
        d[v].append(i)
        
    queue = collections.deque([(0, 0)])
    cost = {}
    
    while queue:
        
        pos, c = queue.popleft()
        
        cost[pos] = c
        if pos == len(arr) - 1: return c
        
        if pos + 1 < len(arr) and c + 1 < cost.get(pos + 1, float('inf')):
            queue.append((pos + 1, c + 1))
            
        if pos - 1 >= 0 and c + 1 < cost.get(pos - 1, float('inf')):
            queue.append((pos - 1, c + 1))
            
        for alt in d[arr[pos]]:
            if cost.get(alt, float('inf')) > c + 1:
                queue.append((alt, c + 1))
    
    return -1