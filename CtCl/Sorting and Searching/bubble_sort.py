# Runtime O(N^2), Space: O(1)
def bubbleSort(nums):

    for i in range(len(nums) - 1):
        for t in range(len(nums) - i - 1):
            if nums[t] > nums[t + 1]:
                nums[t], nums[t + 1] = nums[t + 1], nums[t]

    return nums