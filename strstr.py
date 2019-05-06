# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def strstr(haystack, needle):

    if len(needle) == 0:
        return 0

    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i

    return -1