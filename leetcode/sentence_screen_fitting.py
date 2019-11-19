# Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

# Note:

# A word cannot be split into two lines.
# The order of words in the sentence must remain unchanged.
# Two consecutive words in a line must be separated by a single space.
# Total words in the sentence won't exceed 100.
# Length of each word is greater than 0 and won't exceed 10.
# 1 ≤ rows, cols ≤ 20,000.
# Example 1:

# Input:
# rows = 2, cols = 8, sentence = ["hello", "world"]

# Output: 
# 1

# Explanation:
# hello---
# world---

# The character '-' signifies an empty space on the screen.
# Example 2:

# Input:
# rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

# Output: 
# 2

# Explanation:
# a-bcd- 
# e-a---
# bcd-e-

# The character '-' signifies an empty space on the screen.
# Example 3:

# Input:
# rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

# Output: 
# 1

# Explanation:
# I-had
# apple
# pie-I
# had--

# The character '-' signifies an empty space on the screen.

# TLE
def wordsTyping(self, sentence, rows, cols):
        
    dp = [cols] * rows
    
    iteration = 1
    curr = 0
    
    while curr < len(dp):
        
        s = 0
        while s < len(sentence) and curr < len(dp):
            if dp[curr] >= len(sentence[s]):
                dp[curr] -= (len(sentence[s]) + 1)
                s += 1
            else:
                curr += 1
        
        if s < len(sentence):
            return iteration - 1
        
        iteration += 1

# with additional caching TLE
def wordsTyping(self, sentence, rows, cols):
        
    dp = [cols] * rows
    
    cache = {}
    total_row = 1
    prev = cols
    rest = 0
    i = 0
    
    while i < len(sentence):
        m = sentence[i]
        if len(m) <= prev:
            if prev == cols:
                cache[i] = total_row
            prev = max(0, prev - len(m) - 1)
            i += 1
        else:
            prev = cols
            total_row += 1
        
        if i == len(sentence):
            rest = prev
        
    print(cache, total_row, rest)
    iteration = 1
    curr = 0
    
    while curr < len(dp):
        
        s = 0
        while s < len(sentence) and curr < len(dp):
            if dp[curr] == cols and s in cache:
                curr += total_row - cache[s]
                dp[curr] = rest
                s = len(sentence)
                break
            elif dp[curr] >= len(sentence[s]):
                dp[curr] -= (len(sentence[s]) + 1)
                s += 1
            else:
                curr += 1
        
        if s < len(sentence):
            return iteration - 1
        
        iteration += 1

# caching every calculation result
import functools
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        nwords = len(sentence)
        lengthmap = {i:len(word) for i,word in enumerate(sentence)} # cache word lengths
        
        @functools.lru_cache(None)
        def fitonrow(i): # cache any calls with the same i
            c, completions = 0, 0
            needspace = False
            while c <= cols:
                prevcompletions, previ = completions, i
                if needspace:
                    c += 1
                needspace = True # handle preceeding white space for subsequent words
                c += lengthmap[i]
                i += 1
                if i >= nwords:
                    i = 0
                    completions += 1
            
            return prevcompletions, previ
        
        total = 0
        i = 0
        for r in range(rows):
            completions, newi = fitonrow(i)
            total += completions
            i = newi
        
        return total