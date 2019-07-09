# Runtime O(N^2), Space: O(1)
def selectionSort(nums):

    for i in range(len(nums)):
        min_val = nums[i]
        min_ind = i
        for t in range(i + 1, len(nums)):
            if min_val > nums[t]:
                min_ind = t
                min_val = nums[t]

        nums[i], nums[min_ind] = nums[min_ind], nums[i]

    return nums