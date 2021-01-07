# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


def lengthOfLongestSubstring(self, s):
    if not s:
        return 0

    i, j = 0, 1
    d = {}

    d[s[i]] = i
    max_l = 1

    while j < len(s):
        if s[j] not in d:
            d[s[j]] = j
            j += 1
            max_l = max(max_l, j - i)
        else:
            for t in range(i, d[s[j]]):
                d.pop(s[t], None)

            i, d[s[j]] = d[s[j]] + 1, j
            j += 1

    return max_l


def lengthOfLongestSubstring(self, s: str) -> int:
    d = set()
    i = 0
    max_len = 0

    for j in range(len(s)):
        if s[j] not in d:
            d.add(s[j])
        else:
            while i <= j and s[i] != s[j]:
                d.remove(s[i])
                i += 1
            i += 1
        max_len = max(max_len, j - i + 1)

    return max_len
