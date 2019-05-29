# Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

# We repeatedly make duplicate removals on S until we no longer can.

# Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

 

# Example 1:

# Input: "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

def removeDuplicates(S: str) -> str:

    duplicates = True
    counter = 1

    while duplicates and len(S) > 1:

        for i in range(counter, len(S)):
            if S[i] == S[i - 1]:
                S = S[:i - 1] + S[i + 1:]
                counter = i - 2 if i > 2 else 1
                break
            if i == len(S) - 1:
                duplicates = False

    return S