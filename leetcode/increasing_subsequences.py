# Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2.

 

# Example:

# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
 

# Note:

# The length of the given array will not exceed 15.
# The range of integer in the given array is [-100,100].
# The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.

def findSubsequences(nums):

    if not nums: return 
        
    d = [0] * (len(nums) + 1)
    c = collections.defaultdict(set)
    size = 0
    res = []
    
    for x in nums:
        s = bisect.bisect_right(d[:size], x)
        d[s] = x
        size = max(size, s + 1)
        
        for i in range(s - 1, 0, -1):
            c[i + 1].update([tuple(list(t) + [x]) for t in c[i] if t[-1] <= x])

        c[1].update([tuple([t, x]) for t in c[0] if t <= x])
        c[0].add(x)
    
    for i in range(1, size + 1):
        res += list(c[i])
    
    return res