# Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

# Example 1:

# Input: 12
# Output: 21


# Example 2:

# Input: 21
# Output: -1

def nextGreaterElement(self, n):

    if n <= 10:
        return -1

    n, stack = n // 10, [n % 10]
    found = False

    while n:
        cur, n = n % 10, n // 10
        if cur < stack[-1]:
            found = True
            break
        else:
            stack.append(cur)

    if not found:
        return -1

    ind = bisect.bisect(stack, cur)
    n = n * 10 + stack[ind]
    stack[ind] = cur
    i = 0

    for i in stack:
        n = n * 10 + i

    if n > 2 ** 31 - 1:
        return -1
    return n


def nextGreaterElement(self, n: int) -> int:
    n = list(str(n))

    stack = []
    for i in range(len(n) - 1, 0, -1):
        if n[i] > n[i - 1]:

            t = i
            while t < len(n) and n[i - 1] < n[t]:
                t += 1

            n[t - 1], n[i - 1] = n[i - 1], n[t - 1]
            n[i:] = sorted(n[i:])

            num = int("".join(n))
            return num if num <= 2 ** 31 - 1 else -1 
    return -1
