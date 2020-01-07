# Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array.

# The returned array must be in sorted order.

# Expected time complexity: O(n)

# Example 1:

# Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
# Output: [3,9,15,33]
# Example 2:

# Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
# Output: [-23,-5,1,7]

def sortTransformedArray(self, nums, a, b, c):
        
    if a == 0:
        if b > 0:
            return list(map(lambda x: b * x + c, nums))
        elif b < 0:
            return list(map(lambda x: b * x + c, nums))[::-1]
        else:
            return [c] * len(nums)
    
    res = []
    concavity = True if a > 0 else False
    mid = bisect.bisect_right(nums, -b / (2.0 * a))
    trans = lambda x: a * x ** 2 + b * x + c
    
    i, j = mid - 1, mid
    while i > -1 or j < len(nums):
        if i < 0:
            res.append(trans(nums[j]))
            j += 1
        elif j == len(nums):
            res.append(trans(nums[i]))
            i -= 1
        elif (concavity and trans(nums[i]) < trans(nums[j])) or (not concavity and trans(nums[i]) >= trans(nums[j])):
            res.append(trans(nums[i]))
            i -= 1
        else:
            res.append(trans(nums[j]))
            j += 1
            
    if not concavity:
        res.reverse()
        
        return res