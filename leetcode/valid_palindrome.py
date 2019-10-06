# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.
# Input: "A man, a plan, a canal: Panama"
# Output: true

def isPalindrome(s):

    if s == "":
        return True

    s = ''.join([i for i in s if i.isalpha() or i.isdigit()]).lower()

    for i in range(int(len(s) / 2)):
        if s[i] != s[len(s) - i - 1]:
            return False

    return True