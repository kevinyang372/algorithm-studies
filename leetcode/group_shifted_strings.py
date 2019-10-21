# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

# Example:

# Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# Output: 
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]

def groupStrings(self, strings):
    d = collections.defaultdict(list)
    
    for i in strings:
        if len(i) == 1:
            d[1].append(i)
        else:
            temp = []
            for n in range(1, len(i)):
                if ord(i[n]) >= ord(i[n - 1]):
                    res = ord(i[n]) - ord(i[n - 1])
                else:
                    res = ord(i[n]) + 26 - ord(i[n - 1])
                temp.append(res)
            
            d[len(i), tuple(temp)].append(i)
    
    fin = []
    for t in d:
        fin.append(d[t])
    
    return fin