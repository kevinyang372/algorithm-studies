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

