# There are two anagram strings, what is the minimum swap required to match one string to another. What is the time complexity?
# Example:
# Input: s1 = "AABC", s2 = "AACB"
# Output: 1

import heapq

def minSwap(s1, s2):

    def distance(a, b):
        return sum([1 for i in range(len(a)) if a[i] != b[i]])

    def permutation(p):
        res = set()
        for i in range(len(p)):
            for m in range(i + 1, len(p)):
                temp = list(p)
                temp[i], temp[m] = temp[m], temp[i]
                res.add(tuple(temp))
        return list(res)

    r1, r2 = [], []

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            r1.append(s1[i])
            r2.append(s2[i])

    r1, r2 = tuple(r1), tuple(r2)

    heap = [(0, 0, r1)]
    cost = {r1: 0}

    while heap:
        cur_cost, dis, cur = heapq.heappop(heap)
        if cur == r2: return dis
        for var in permutation(cur):
            new_cost = dis + 1 + distance(var, r2)
            if new_cost < cost.get(var, float('inf')):
                cost[var] = new_cost
                heapq.heappush(heap, (new_cost, dis + 1, var))

    return -1


