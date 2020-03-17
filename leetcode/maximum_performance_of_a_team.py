# There are n engineers numbered from 1 to n and two arrays: speed and efficiency, where speed[i] and efficiency[i] represent the speed and efficiency for the i-th engineer respectively. Return the maximum performance of a team composed of at most k engineers, since the answer can be a huge number, return this modulo 10^9 + 7.

# The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers. 

 

# Example 1:

# Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
# Output: 60
# Explanation: 
# We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.
# Example 2:

# Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
# Output: 68
# Explanation:
# This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.
# Example 3:

# Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
# Output: 72
 

# Constraints:

# 1 <= n <= 10^5
# speed.length == n
# efficiency.length == n
# 1 <= speed[i] <= 10^5
# 1 <= efficiency[i] <= 10^8
# 1 <= k <= n

def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
    d = collections.defaultdict(list)
    for i, v in enumerate(speed):
        d[efficiency[i]].append(v)
        
    queue = []
    max_val = 0
    curr_sum = 0
    
    for t in sorted(list(d.keys()), reverse = True):
        for e in d[t]:
            if len(queue) < k:
                heapq.heappush(queue, e)
                curr_sum += e
            elif e > queue[0]:
                curr_sum -= queue[0]
                heapq.heappushpop(queue, e)
                curr_sum += e
                
        max_val = max(max_val, t * curr_sum)
    
    return max_val % (10**9 + 7)