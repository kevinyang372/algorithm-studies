# There are 𝑛 piranhas with sizes 𝑎1,𝑎2,…,𝑎𝑛 in the aquarium. Piranhas are numbered from left to right in order they live in the aquarium.

# Scientists of the Berland State University want to find if there is dominant piranha in the aquarium. The piranha is called dominant if it can eat all the other piranhas in the aquarium (except itself, of course). Other piranhas will do nothing while the dominant piranha will eat them.

# Because the aquarium is pretty narrow and long, the piranha can eat only one of the adjacent piranhas during one move. Piranha can do as many moves as it needs (or as it can). More precisely:

# The piranha 𝑖 can eat the piranha 𝑖−1 if the piranha 𝑖−1 exists and 𝑎𝑖−1<𝑎𝑖.
# The piranha 𝑖 can eat the piranha 𝑖+1 if the piranha 𝑖+1 exists and 𝑎𝑖+1<𝑎𝑖.
# When the piranha 𝑖 eats some piranha, its size increases by one (𝑎𝑖 becomes 𝑎𝑖+1).

# Your task is to find any dominant piranha in the aquarium or determine if there are no such piranhas.

# Note that you have to find any (exactly one) dominant piranha, you don't have to find all of them.

# For example, if 𝑎=[5,3,4,4,5], then the third piranha can be dominant. Consider the sequence of its moves:

# The piranha eats the second piranha and 𝑎 becomes [5,5⎯⎯,4,5] (the underlined piranha is our candidate).
# The piranha eats the third piranha and 𝑎 becomes [5,6⎯⎯,5].
# The piranha eats the first piranha and 𝑎 becomes [7⎯⎯,5].
# The piranha eats the second piranha and 𝑎 becomes [8⎯⎯].
# You have to answer 𝑡 independent test cases.

# Input
# The first line of the input contains one integer 𝑡 (1≤𝑡≤2⋅104) — the number of test cases. Then 𝑡 test cases follow.

# The first line of the test case contains one integer 𝑛 (2≤𝑛≤3⋅105) — the number of piranhas in the aquarium. The second line of the test case contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 (1≤𝑎𝑖≤109), where 𝑎𝑖 is the size of the 𝑖-th piranha.

# It is guaranteed that the sum of 𝑛 does not exceed 3⋅105 (∑𝑛≤3⋅105).

# Output
# For each test case, print the answer: -1 if there are no dominant piranhas in the aquarium or index of any dominant piranha otherwise. If there are several answers, you can print any.

# Example
# inputCopy
# 6
# 5
# 5 3 4 4 5
# 3
# 1 1 1
# 5
# 4 4 3 4 4
# 5
# 5 5 4 3 2
# 3
# 1 1 2
# 5
# 5 4 3 5 5
# outputCopy
# 3
# -1
# 4
# 3
# 3
# 1
# Note
# The first test case of the example is described in the problem statement.

# In the second test case of the example, there are no dominant piranhas in the aquarium.

# In the third test case of the example, the fourth piranha can firstly eat the piranha to the left and the aquarium becomes [4,4,5,4], then it can eat any other piranha in the aquarium.


