# Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
# A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

# Example:
# Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
#  "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
# Note:
# The number of elements of the given array will not exceed 10,000
# The length sum of elements in the given array will not exceed 600,000.
# All the input string will only include lower case letters.
# The returned elements order does not matter.

def findAllConcatenatedWordsInADict(self, words):
        
    words = set(words)
    
    def search(w):
        for i in range(1, len(w)):
            if w[:i] in words and (w[i:] in words or search(w[i:])):
                return True
        return False
    
    return [word for word in words if search(word)]