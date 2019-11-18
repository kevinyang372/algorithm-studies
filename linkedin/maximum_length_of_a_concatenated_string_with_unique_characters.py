# Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

# Return the maximum possible length of s.

 

# Example 1:

# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
# Maximum length is 4.
# Example 2:

# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible solutions are "chaers" and "acters".
# Example 3:

# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
 

# Constraints:

# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] contains only lower case English letters.

def maxLength(self, arr):
    
    arr = [[set(i)] for i in arr if len(set(i)) == len(i)]
    
    if not arr: return 0
    
    max_length = len(arr[0][0])
    
    for t in range(1, len(arr)):
        temp = arr[t][0]
        for i in range(t):
            for instance in arr[i]:
                if not temp.intersection(instance):
                    t2 = set(temp)
                    t2.update(instance)
                    arr[t].append(t2)
        max_length = max(max_length, max([len(s) for s in arr[t]]))
        
    return max_length