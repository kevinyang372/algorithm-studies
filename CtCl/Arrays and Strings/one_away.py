# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

def one_away(str1, str2):

    if abs(len(str1) - len(str2)) > 1: return False

    if len(str1) == len(str2):
        count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                if count == 1:
                    return False
                count += 1

        return True
    elif len(str1) > len(str2):
        for i in range(len(str1) - 1):
            if str1[i] != str2[i]:
                if str1[i + 1:] != str2[i:]:
                    return False

        return True
    else:
        for i in range(len(str2) - 1):
            if str2[i] != str1[i]:
                if str2[i + 1:] != str1[i:]:
                    return False

        return True
