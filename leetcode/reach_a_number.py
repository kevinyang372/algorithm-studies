# You are standing at position 0 on an infinite number line. There is a goal at position target.

# On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

# Return the minimum number of steps required to reach the destination.

# Example 1:
# Input: target = 3
# Output: 2
# Explanation:
# On the first move we step from 0 to 1.
# On the second step we step from 1 to 3.
# Example 2:
# Input: target = 2
# Output: 3
# Explanation:
# On the first move we step from 0 to 1.
# On the second move we step  from 1 to -1.
# On the third move we step from -1 to 2.
# Note:
# target will be a non-zero integer in the range [-10^9, 10^9].


def reachNumber(self, target: int) -> int:
    target = abs(target)
    mn, mx = 1, target + 1
    mid = (mn + mx) // 2

    while mn < mx:
        mid = (mn + mx) // 2
        if (mid + 1) * mid / 2 < target:
            mn = mid + 1
        elif (mid + 1) * mid / 2 == target:
            return mid
        else:
            mx = mid

    total = (mn + 1) * mn / 2

    while (total - target) % 2 != 0:
        mn += 1
        total = (mn + 1) * mn / 2

    return mn
