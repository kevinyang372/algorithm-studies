# Given a string containing only digits, restore it by returning all possible valid IP address combinations.

# Example:

# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]

def restoreIpAddresses(s):
    return restoreIpAddress(s, 4)

def restoreIpAddress(s, num):

    if num == 1:
        if len(s) == 0 or int(s) > 255 or (len(s) > 1 and int(s[0]) == 0):
            return False
        else:
            return [s]
    elif len(s) < num:
        return False

    result = []

    temp_0 = restoreIpAddress(s[1:], num - 1)
    if temp_0:
        for i in temp_0:
            result.append("%s.%s" % (s[0], i))
    

    if len(s) > 2 and s[0] != '0':
        temp_1 = restoreIpAddress(s[2:], num - 1)
        if temp_1:
            for i in temp_1:
                result.append("%s.%s" % (s[:2], i))

    if len(s) > 2 and s[0] != '0' and int(s[:3]) < 256:
        temp_2 = restoreIpAddress(s[3:], num - 1)
        if temp_2:
            for i in temp_2:
                result.append("%s.%s" % (s[:3], i))

    return result
