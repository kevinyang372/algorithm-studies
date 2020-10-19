# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

# Example:

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

# Output: ["AAAAACCCCC", "CCCCCAAAAA"]

# O(N^2)
def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
    if len(s) < 10: return
    res = set()
    
    def kmp(s, target):
        dp = [0] * len(target)
        
        for i, v in enumerate(target):
            if i > 0 and v == target[dp[i - 1]]:
                dp[i] = dp[i - 1] + 1
         
        i = j = 0
        while i < len(s):
            if s[i] == target[j]:
                i += 1
                j += 1
                
                if j == len(target):
                    return True
            elif j > 0:
                j = dp[j - 1]
            else:
                i += 1
            
    for sub in range(len(s) - 10):
        if kmp(s[sub + 1:], s[sub:sub + 10]):
            res.add(s[sub:sub + 10])
            
    return res

# O(N)
def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
    if len(s) < 10: return
    seen, res = set(), set()
    
    for sub in range(len(s) - 9):
        if s[sub:sub + 10] in seen:
            res.add(s[sub:sub + 10])
        else:
            seen.add(s[sub:sub + 10])
            
    return res

# rolling hash
def findRepeatedDnaSequences(self, s: str) -> List[str]:
    if len(s) < 10: return
    
    letter_to_num = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    r = {}
    
    res = 0
    for i in range(10):
        res *= 10
        res += letter_to_num[s[i]]
    
    d = collections.Counter()
    d[res] += 1
    
    for j in range(10, len(s)):
        res %= 10 ** 9
        res *= 10
        res += letter_to_num[s[j]]
        
        d[res] += 1
        if res not in r:
            r[res] = j
    
    dnas = [i for i in d if d[i] > 1]
    return [s[r[dna] - 9:r[dna] + 1] for dna in dnas]