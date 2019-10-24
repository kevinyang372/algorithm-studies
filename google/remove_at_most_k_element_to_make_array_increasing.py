# Question : given an array, please check if we can remove at most one element to make it strictly increasing.

# ie1. [1,2,3,7,5,6], TRUE
# ie2. [1,2,3,7,8,4,5] FALSE
# follow up, what if at most 2?
# follow up, what if K?

# recursive approach
def removeKElements(arr, k):
    if len(arr) < 2: return True
    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            if k == 0:
                return False
            else:
                temp = arr[:]
                temp.pop(i)

                j = i - 1
                while j > -1 and arr[j] >= arr[i]:
                    j -= 1

                return removeKElements(temp, k - 1) or removeKElements(arr[:j + 1] + arr[i:], k - i + j + 1)
    
    return True

# LIS
def removeKElements(arr, k):
    if len(arr) < 2: return True

    dp = [1] * len(arr)
    max_len = 1

    for j in range(1, len(arr)):
        for i in range(j):
            if arr[j] > arr[i]:
                dp[j] = max(dp[j], dp[i] + 1)
                max_len = max(max_len, dp[j])

    return len(arr) - max_len <= k