# Given a string, determine if a permutation of the string could form a palindrome.

# Example 1:

# Input: "code"
# Output: false
# Example 2:

# Input: "aab"
# Output: true
# Example 3:

# Input: "carerac"
# Output: true

def canPermutePalindrome(self, s: str) -> bool:
    c = 0
    for x, y in collections.Counter(s).items():
        if y % 2 != 0:
            if c == 1:
                return False
            c += 1
    return True