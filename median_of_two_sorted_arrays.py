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