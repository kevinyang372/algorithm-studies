# Given two lists of equal length
# lis1 = [-1, 3, 8, 2, 9, 5]
# lis2 = [4, 1, 2, 10, 5, 20]
# And a target (e.g. 24)
# Return the closest sum of two elements from each list to the target

def sum_of_two_numbers(lis1, lis2, target):
    
    closest = abs(lis1[0] + lis2[0] - target)
    sums = lis2[0] + lis1[0]
    
    for i in lis1:
        for t in lis2:

            now_closest = abs(t + i - target)

            if now_closest < closest:
                closest = now_closest
                sums = i + t

    return sums