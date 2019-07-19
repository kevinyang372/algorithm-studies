# Question: Can you break the given string into words, provided by a given hashmap of frequency of word as <word: n>

# Example 1:

# HashMap -> {"abc":3, "ab":2, "abca":1}
# String: "abcabcabcabca"
# Output: true
# Explanation: "abc" + "abc" + "abc" + "abca"
# Example 2:

# HashMap -> {"abc":3, "ab":2}
# String: "abcabab"
# Output: true
# Explanation: "abc" + "ab" + "ab"
# Example 3:

# HashMap -> {"abc":3, "ab":2, "abca":1}
# String: "abcx"
# Output: false

def wordBreak(m, s):

    if not m: return False
    if s in m and m[s] > 0: return True

    for i in range(1, len(s)):
        if s[:i] in m and m[s[:i]] > 0:
            m[s[:i]] -= 1
            if wordBreak(m, s[i:]):
                return True
            m[s[:i]] += 1

    return False