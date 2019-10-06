# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

# Note:
# You may assume that both strings contain only lowercase letters.

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

def canConstruct(self, ransomNote, magazine):
    if len(ransomNote) > len(magazine): return False
    
    m = collections.Counter(magazine)
    
    for i in ransomNote:
        if i in m and m[i] > 0:
            m[i] -= 1
        else:
            return False
        
    return True