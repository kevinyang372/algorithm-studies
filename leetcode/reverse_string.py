# Reverse String
# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

def reverse_string(str1):

    i = 0
    j = len(str1) - 1

    while i < j:

        temp = str1[i]
        str1[i] = str1[j]
        str1[j] = temp

        i += 1
        j -= 1

    return str1


def reverseString(self, s: List[str]) -> None:
        
    for i in range(len(s) // 2):
        s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
        
    return s