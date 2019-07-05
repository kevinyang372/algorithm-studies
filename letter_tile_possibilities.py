# You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.

 

# Example 1:

# Input: "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
# Example 2:

# Input: "AAABBC"
# Output: 188
 

# Note:

# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.

def numTilePossibilities(self, tiles):
        
    stack = set()
    
    for i in tiles:
        temp = [i]
        for m in stack:
            for l in range(len(m) + 1):
                temp.append("%s%s%s" % (m[:l], i, m[l:]))
        for k in temp:
            stack.add(k)
            
    return len(list(stack))