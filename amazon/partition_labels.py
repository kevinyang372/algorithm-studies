# A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

# Example 1:
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
# Note:

# S will have length in range [1, 500].
# S will consist of lowercase letters ('a' to 'z') only.

cache = {}

def partitionLabels(S):

    if S[0] == S[-1] or len(S) < 2: return [len(S)]
    if S in cache: return cache[S]

    min_list = [len(S)]
    for i in range(1, len(S)):
        if set(sorted(S[:i])).isdisjoint(sorted(S[i:])):
            temp = partitionLabels(S[:i]) + partitionLabels(S[i:])
            min_list = max(min_list, temp, key=len)

    cache[S] = min_list
    return min_list

# O(N) Time O(N) Space
def partitionLabels(S):

    dic = {}
    for k, v in enumerate(S):
        dic[v] = k

    res = []
    count = 0
    cur_max = 0

    for k, v in enumerate(S):
        count += 1
        cur_max = max(cur_max, dic[v])

        if k == cur_max:
            res.append(count)
            count = 0

    return res

# solve with intervals
def partitionLabels(self, S):
        
    intervals = []
    d = {}
    
    for i, v in enumerate(S):
        if v in d:
            intervals[d[v]][1] = i
        else:
            d[v] = len(intervals)
            intervals.append([i, i])
    
    m = 0
    while m < len(intervals) - 1:
        if intervals[m][1] > intervals[m + 1][0]:
            intervals[m] = [intervals[m][0], max(intervals[m + 1][1], intervals[m][1])]
            intervals.pop(m + 1)
        else:
            m += 1
    
    return [y - x + 1 for (x, y) in intervals]