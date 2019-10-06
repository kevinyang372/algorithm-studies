# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# Example:

# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:

# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

# hashmap and heap
def minWindow(self, s, t):
        
    d = collections.defaultdict(list)
    mapping = {}
    arr = []
    
    for i,v in enumerate(t):
        if v not in d:
            mapping[v] = len(arr)
            arr.append(-1)
        d[v].append(-1)
            
    min_window = ''
    min_val = float('inf')
    
    for ind, i in enumerate(s):
        if i in d:
            heapq.heappushpop(d[i], ind)
            arr[mapping[i]] = d[i][0]
            
            temp = min(arr)
            if temp == -1:
                continue
            elif ind - temp + 1 < min_val:
                min_val = ind - temp + 1
                min_window = s[temp:ind + 1]
    
    return min_window

# sliding window
def minWindow(self, s, t):
        
    if not s or not t: return ''
    
    l = r = 0
    ans = (float('inf'), 0, 0)
    
    dic = collections.Counter(t)
    required = len(dic)
    formed = 0

    window = collections.defaultdict(int)
    
    while r < len(s):
        cur = s[r]
        window[cur] += 1

        if cur in dic and window[cur] == dic[cur]:
            formed += 1

        if formed == required:
            while l <= r and formed == required:
                window[s[l]] -= 1

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                if s[l] in dic and window[s[l]] < dic[s[l]]:
                    formed -= 1

                l += 1
        r += 1
    
    return '' if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]
