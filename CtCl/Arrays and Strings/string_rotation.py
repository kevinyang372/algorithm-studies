# Assume you have amethod isSubstring which checks ifone word is asubstring of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one call to isSubstring (e.g.,"waterbottle"is a rotation of"erbottlewat").

def isSubstring(string, sub):
    return string.find(sub) != -1

def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return isSubstring(s1 + s1, s2)
    return False