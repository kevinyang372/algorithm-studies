# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

# A string is represented by an array if the array elements concatenated in order forms the string.


# Example 1:

# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.
# Example 2:

# Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
# Output: false
# Example 3:

# Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
# Output: true


# Constraints:

# 1 <= word1.length, word2.length <= 103
# 1 <= word1[i].length, word2[i].length <= 103
# 1 <= sum(word1[i].length), sum(word2[i].length) <= 103
# word1[i] and word2[i] consist of lowercase letters.


def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
    word2_ind = word2_ind_ind = 0
    for ind in range(len(word1)):
        for j in range(len(word1[ind])):
            if word2_ind == len(word2) or word1[ind][j] != word2[word2_ind][word2_ind_ind]:
                return False

            if word2_ind_ind == len(word2[word2_ind]) - 1:
                word2_ind += 1
                word2_ind_ind = 0
            else:
                word2_ind_ind += 1

    if word2_ind < len(word2):
        return False
    return True
