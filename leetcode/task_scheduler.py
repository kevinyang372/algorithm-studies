# Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

# However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

# You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

# Example:

# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

import collections

# Greedy -- doesn't work. We need to optimize based on the number of instances
def leastInterval(tasks, n):

    if n == 0: return len(tasks)

    interval = collections.Counter()
    total = collections.Counter(tasks)

    for i in total.keys():
        interval[i] = 0

    res = []
    while total:
        found = False
        fin = []
        for k, v in interval.items():
            if v <= 0 and not found:
                res.append(k)
                total[k] -= 1

                if total[k] == 0:
                    fin.append(k)

                interval[k] = n
                found = True
            else:
                interval[k] -= 1

        for i in fin:
            total.pop(i)
            interval.pop(i)

        if not found:
            res.append('idle')
    
    return res


# priority queue
def leastInterval(self, tasks: List[str], n: int) -> int:
        d = collections.Counter(tasks)
        
        available = [(-d[task], task) for task in d]
        on_cooldown = collections.deque()
        
        heapq.heapify(available)
        i = 0
        
        while available or on_cooldown:
            while on_cooldown and on_cooldown[0][0] <= i:
                _, task = on_cooldown.popleft()
                heapq.heappush(available, (-d[task], task))
            
            if not available:
                i += 1
                continue
                
            _, task_name = heapq.heappop(available)
            d[task_name] -= 1
            
            if d[task_name] != 0:
                on_cooldown.append((i + n + 1, task_name))
            
            i += 1
        
        return i


from heapq import heappush, heappop
from collections import Counter

def leastInterval(self, tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    curr_time, h = 0, []
    for k,v in Counter(tasks).items():
        heappush(h, (-1*v, k))
    while h:
        i, temp = 0, []
        while i <= n:
            curr_time += 1
            if h:
                x,y = heappop(h)
                if x != -1:
                    temp.append((x+1,y))
            if not h and not temp:
                break
            else:
                i += 1
        for item in temp:
            heappush(h, item)
    return curr_time

#