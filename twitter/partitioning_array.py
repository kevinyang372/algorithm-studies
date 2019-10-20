# Given an array of numbers, you are required to check if it is possible to partition the array into some subsequences of length k each, such that:
# - Each element in the array occurs in exactly one subsequence
# - All the numbers in a subsequence are distinct
# - Elements in the array having the same value must be in different subsequnces

# Is it possible to partition the array satisfying the above conditions?

def partitionArray(arr, k):
    if len(arr) % k != 0: return False

    d = collections.Counter()
    for i in arr:
        d[i] += 1
        if d[i] > len(arr) // k:
            return False

    return True