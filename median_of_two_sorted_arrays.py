# Median of Two Sorted Arrays
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).


# Brute-force
def median_of_two_sorted(lis1, lis2):

    total_len = len(lis1) + len(lis2)
    med = int((total_len - 1) / 2)

    i = -1
    j = -1

    while i + j < med - 1:

        if i == len(lis1) - 1:
            j += 1
            res = lis2[j]
        elif j == len(lis2) - 1:
            i += 1
            res = lis1[i]
        else:
            if lis1[i + 1] > lis2[j + 1]:
                j += 1
                res = lis2[j]
            else:
                i += 1
                res = lis1[i]

    if total_len % 2 == 0:

        if i == len(lis1) - 1:
            j += 1
            res2 = lis2[j]
        elif j == len(lis2) - 1:
            i += 1
            res2 = lis1[i]
        else:
            if lis1[i + 1] > lis2[j + 1]:
                j += 1
                res2 = lis2[j]
            else:
                i += 1
                res2 = lis1[i]

        res = (res + res2) / 2

    return res

# Binary O(logN)
def findMedianSortedArrays(nums1, nums2):

    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    total = len(nums1) + len(nums2)

    if not nums1:
        if len(nums2) % 2 == 1:
            return nums2[len(nums2) // 2]
        else:
            return (nums2[len(nums2) // 2 - 1] + nums2[len(nums2) // 2]) / 2.0
        
    if nums1[0] >= nums2[-1]:
        if total % 2 == 1:
            return nums2[total // 2]
        else:
            if len(nums1) == len(nums2):
                return (nums1[0] + nums2[-1]) / 2.0
            else:
                return (nums2[total // 2] + nums2[(total - 1) // 2]) / 2.0
    elif nums1[-1] <= nums2[0]:
        if total % 2 == 1:
            return nums2[total // 2 - len(nums1)]
        else:
            if len(nums1) == len(nums2):
                return (nums1[-1] + nums2[0]) / 2.0
            else:
                return (nums2[total // 2 - len(nums1)] + nums2[(total - 1) // 2 - len(nums1)]) / 2.0

    i = len(nums1) // 2
    j = total // 2 - i

    lower, upper = 0, len(nums1)

    while max(nums1[i - 1], nums2[j - 1]) > min(nums1[i], nums2[j]):
        print(i, j)
        if nums1[i - 1] > nums2[j]:
            upper = i
        else:
            lower = i + 1
        i = (lower + upper) // 2
        j = total // 2 - i

    if total % 2 == 1:
        return min(nums1[i], nums2[j])
    else:
        return (max(nums1[i - 1], nums2[j - 1]) + min(nums1[i], nums2[j])) / 2.0