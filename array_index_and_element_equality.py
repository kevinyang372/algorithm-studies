# Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch that returns the lowest index i for which arr[i] == i. Return -1 if there is no such index. Analyze the time and space complexities of your solution and explain its correctness.

# Examples:

# input: arr = [-8,0,2,5]
# output: 2 # since arr[2] == 2

# input: arr = [-1,0,3,6]
# output: -1 # since no index in arr satisfies 

def index_equals_value_search(arr):
    if not arr: return -1
  
    i, j = 0, len(arr)
    min_val = float('inf')
  
    while i < j:
        mid = (i + j) // 2
        if arr[mid] == mid:
            min_val = min(min_val, mid)
        if arr[mid] >= mid:
            j = mid
        else:
            i = mid + 1
  
    return -1 if min_val == float('inf') else min_val