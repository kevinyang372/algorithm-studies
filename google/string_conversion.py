# Given 2 strings s and t, determine if you can convert s into t. The rules are:

# You can change 1 letter at a time.
# Once you changed a letter you have to change all occurrences of that letter.
# Example 1:

# Input: s = "abca", t = "dced"
# Output: true
# Explanation: abca ('a' to 'd') -> dbcd ('c' to 'e') -> dbed ('b' to 'c') -> dced
# Example 2:

# Input: s = "ab", t = "ba"
# Output: true
# Explanation: ab -> ac -> bc -> ba
# Example 3:

# Input: s = "abcdefghijklmnopqrstuvwxyz", t = "bcdefghijklmnopqrstuvwxyza"
# Output: false
# Example 4:

# Input: s = "aa", t = "cd"
# Output: false
# Example 5:

# Input: s = "ab", t = "aa"
# Output: true
# Example 6:

# Input: s = "abcdefghijklmnopqrstuvwxyz", t = "bbcdefghijklmnopqrstuvwxyz"
# Output: true
# Both strings contain only lowercase English letters.

def stringConversion(s, t):

    if len(s) != len(t): return False
    if len(set(s)) == len(set(t)) == 26: return s == t
    
    word_num = {}
    num_word = {}

    for i, v in enumerate(s):
        if v not in word_num:
            encrypt_to = ord(t[i])
            word_num[v] = encrypt_to

            if encrypt_to == ord(v): continue
            if encrypt_to in num_word: return False
            num_word[encrypt_to] = v
        else:
            if word_num[v] != ord(t[i]): return False

    return True