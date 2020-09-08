# Given a string s and an array of integers cost where cost[i] is the cost of deleting the character i in s.

# Return the minimum cost of deletions such that there are no two identical letters next to each other.

# Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.

 

# Example 1:

# Input: s = "abaac", cost = [1,2,3,4,5]
# Output: 3
# Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).
# Example 2:

# Input: s = "abc", cost = [1,2,3]
# Output: 0
# Explanation: You don't need to delete any character because there are no identical letters next to each other.
# Example 3:

# Input: s = "aabaa", cost = [1,2,3,4,1]
# Output: 2
# Explanation: Delete the first and the last character, getting the string ("aba").
 

# Constraints:

# s.length == cost.length
# 1 <= s.length, cost.length <= 10^5
# 1 <= cost[i] <= 10^4
# s contains only lowercase English letters.

def minCost(self, s: str, cost: List[int]) -> int:
    if not s: return 0

    # [current character, maximum, current sum, length]
    stack = [s[0], cost[0], cost[0], 1]
    res = 0

    for i in range(1, len(s)):
        if s[i] != stack[0]:
            if stack[3] != 1:
                res += stack[2] - stack[1]

            stack = [s[i], cost[i], cost[i], 1]
        else:
            stack[1] = max(cost[i], stack[1])
            stack[2] += cost[i]
            stack[3] += 1

    if stack[3] != 1:
        res += stack[2] - stack[1]

    return res