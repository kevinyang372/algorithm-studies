# We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

# Return a list of all uncommon words. 

# You may return the list in any order.

 

# Example 1:

# Input: A = "this apple is sweet", B = "this apple is sour"
# Output: ["sweet","sour"]
# Example 2:

# Input: A = "apple apple", B = "banana"
# Output: ["banana"]
 

# Note:

# 0 <= A.length <= 200
# 0 <= B.length <= 200
# A and B both contain only spaces and lowercase letters.

def uncommonFromSentences(self, A: str, B: str) -> List[str]:
    in_A = collections.Counter(A.split(' '))
    in_B = collections.Counter(B.split(' '))
    
    res = []
    
    for x, y in in_A.items():
        if y == 1 and x not in in_B:
            res.append(x)
            
    for x, y in in_B.items():
        if y == 1 and x not in in_A:
            res.append(x)
            
    return res