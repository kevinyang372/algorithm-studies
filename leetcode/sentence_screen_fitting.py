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