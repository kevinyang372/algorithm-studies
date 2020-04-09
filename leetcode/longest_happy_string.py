# A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.

# Given three integers a, b and c, return any string s, which satisfies following conditions:

# s is happy and longest possible.
# s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
# s will only contain 'a', 'b' and 'c' letters.
# If there is no such string s return the empty string "".

 

# Example 1:

# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.
# Example 2:

# Input: a = 2, b = 2, c = 1
# Output: "aabbc"
# Example 3:

# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# Explanation: It's the only correct answer in this case.
 

# Constraints:

# 0 <= a, b, c <= 100
# a + b + c > 0

# TLE
def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
    d = {}
    def construct(da, db, dc, prev):
        if (da, db, dc, prev) in d: return d[da, db, dc, prev]
        l = ''
        if da > 0 and prev != 'a':
            l = max('a' + construct(da - 1, db, dc, 'a'), l, key=len)
        if da > 1 and prev != 'a':
            l = max('aa' + construct(da - 2, db, dc, 'a'), l, key=len)
        if db > 0 and prev != 'b':
            l = max('b' + construct(da, db - 1, dc, 'b'), l, key=len)
        if db > 1 and prev != 'b':
            l = max('bb' + construct(da, db - 2, dc, 'b'), l, key=len)
        if dc > 0 and prev != 'c':
            l = max('c' + construct(da, db, dc - 1, 'c'), l, key=len)
        if dc > 1 and prev != 'c':
            l = max('cc' + construct(da, db, dc - 2, 'c'), l, key=len)
            
        d[da, db, dc, prev] = l
        return l
    
    return construct(a, b, c, '')

# heap
def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
    q = []
    
    if a > 0: q.append((-a, 'a'))
    if b > 0: q.append((-b, 'b'))
    if c > 0: q.append((-c, 'c'))
    
    heapq.heapify(q)
    res = ''
    
    while len(q) > 1:
        h = heapq.heappop(q)
        l = heapq.heappop(q)
        
        print(h, l)
        
        hval, hchar = -h[0], h[1]
        lval, lchar = -l[0], l[1]
        
        if hval >= 2:
            res += hchar * 2
            hval -= 2
        else:
            res += hchar
            hval -= 1
        
        if lval <= -h[0] // 2 or lval == 1:
            res += lchar
            lval -= 1
        else:
            res += lchar * 2
            lval -= 2
        
        if hval > 0: heapq.heappush(q, (-hval, hchar))
        if lval > 0: heapq.heappush(q, (-lval, lchar))
    
    if q and res[-1] != q[0][1]: res += q[0][1] * min(2, -q[0][0])
        
    return res