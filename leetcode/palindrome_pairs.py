# Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

# Example 1:

# Input: ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]] 
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
# Example 2:

# Input: ["bat","tab","cat"]
# Output: [[0,1],[1,0]] 
# Explanation: The palindromes are ["battab","tabbat"]

def palindromePairs(self, words):
        
    def is_palindrome(check):
        return check == check[::-1]

    words = {word: i for i, word in enumerate(words)}
    valid_pals = []
    for word, k in words.iteritems():
        n = len(word)
        for j in range(n+1):
            pref = word[:j]
            suf = word[j:]
            if is_palindrome(pref):
                back = suf[::-1]
                if back != word and back in words:
                    valid_pals.append([words[back],  k])
            if j != n and is_palindrome(suf):
                back = pref[::-1]
                if back != word and back in words:
                    valid_pals.append([k, words[back]])
    return valid_pals