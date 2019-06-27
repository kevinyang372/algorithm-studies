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


# Priority Queue, somehow didn't work

def leastInterval(self, tasks, n):
    if n == 0: return len(tasks)

    interval = collections.Counter()
    total = collections.Counter(tasks)
    prior = []

    for i in total.keys():
        interval[i] = 0
        prior.append([total[i], i])

    res = 0
    prior.sort(reverse=True)
    
    while prior:
        found = False
        fin = []
        for v, k in enumerate(prior):
            if interval[k[1]] <= 0 and not found:
                res += 1
                prior[v][0] -= 1

                if prior[v][0] == 0:
                    fin.append(k)

                interval[k[1]] = n
                found = True
            else:
                interval[k[1]] -= 1

        for i in fin:
            prior.remove(i)
            prior.sort(reverse=True)
            interval.pop(i[1])

        if not found:
            res += 1
    
    return res

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