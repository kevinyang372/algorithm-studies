# Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

# For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.

# For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

# Given a list of query words, return the number of words that are stretchy. 

 

# Example:
# Input: 
# S = "heeellooo"
# words = ["hello", "hi", "helo"]
# Output: 1
# Explanation: 
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
 

# Notes:

# 0 <= len(S) <= 100.
# 0 <= len(words) <= 100.
# 0 <= len(words[i]) <= 100.
# S and all words in words consist only of lowercase letters

def expressiveWords(self, S, words):
        
    def process(word):
        
        lis = []
        pre, count = None, 0
        
        for char in word:
            if not pre:
                pre = char
            elif pre != char:
                pre = char
                lis.append((pre, count))
                count = 0                    
            count += 1
            
        lis.append((pre, count))
        return lis
    
    def examine(l1, l2):
        if len(l1) != len(l2): return False
        
        for (v1, c1), (v2, c2) in zip(l1, l2):
            if v1 == v2 and ((c1 <= c2 and c2 >= 3) or (c1 == c2 and c2 < 3)):
                continue
            return False
        
        return True
    
    org = process(S)
    return sum([1 for word in words if examine(process(word), org)])