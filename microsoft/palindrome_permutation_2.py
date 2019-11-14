# Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

# Example 1:

# Input: "aabb"
# Output: ["abba", "baab"]
# Example 2:

# Input: "abc"
# Output: []

def generatePalindromes(self, s):
    if len(s) == 1: return [s]
    
    c = collections.Counter(s)
    
    res = collections.Counter()
    alone = ''
    
    for i in c:
        if c[i] % 2 == 1 and len(alone) > 0:
            return
        elif c[i] % 2 == 1:
            alone = i
            
            if c[i] // 2 > 0:
                res[i] += c[i] // 2
        else:
            res[i] += c[i] // 2
            
    seen = set()
    
    def findPermutations(arr):
        if not arr: return ['']
        
        temp = []
        for i in arr:
            arr[i] -= 1
            if arr[i] == 0: arr.pop(i)
            
            temp += [i + t for t in findPermutations(arr)]
            arr[i] += 1
        
        return set(temp)
    
    return [t + alone + t[::-1] for t in findPermutations(res)]