# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

# Example:

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

# Output: ["AAAAACCCCC", "CCCCCAAAAA"]

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