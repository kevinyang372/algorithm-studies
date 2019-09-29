# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Input: word1 = “coding”, word2 = “practice”
# Output: 3
# Input: word1 = "makes", word2 = "coding"
# Output: 1
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

def shortestDistance(words, word1, word2):
    if not words: return 0
    
    i = j = 0
    move_i = True
    shortest_distance = float('inf')
    
    while i < len(words) and j < len(words):
        if move_i:
            if words[i] == word1:
                if words[j] == word2:
                    shortest_distance = min(shortest_distance, abs(j - i))
                    
                
                if i >= j:
                    move_i = False
                    j += 1
                else:
                    i += 1
            else:
                i += 1
        else:
            if words[j] == word2:
                if words[i] == word1:
                    shortest_distance = min(shortest_distance, abs(j - i))

                    
                if j >= i:
                    move_i = True
                    i += 1
                else:
                    j += 1
            else:
                j += 1
                
    return shortest_distance