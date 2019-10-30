# You start at index 0 in an array with length 'h'. At each step, you can move to the left, move to the right, or stay in the same place(Note! Stay in the same place also takes one step). How many possible ways are you still at index 0 after you have walked 'n' step?

# Example： n = 3
# 1. right->left->stay
# 2. right->stay->left
# 3. stay->right->left
# 4. stay->stay->stay

# Can anyone solve it in n^2

def countZero(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for it in range(n):
        temp = [0] * (n + 1)
        for i in range(it + 1):
            for di in [-1, 0, 1]:
                if i + di >= 0:
                    temp[i + di] += dp[i]
        dp = temp
    
    return dp[0]