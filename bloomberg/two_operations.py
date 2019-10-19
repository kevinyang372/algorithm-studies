# Assume you have a CPU, where you can use only 2 operations - multiply by 2 or integer division by 3. Please calculate the minimum number of steps required to generate 'n' from 1.
# Note - division by 3 is an integer, that is, 10 / 3 = 3
# eg: 10 - 1 X 2 X 2 X 2 X 2 / 3 X 2
# Ans - 6 steps, as we have used 5 multiplications by 2, and one division by 3
# eg: 3 - 1 X 2 X 2 X 2 X 2 X 2 / 3 / 3
# Ans - 7 steps, as we have used 5 multiplications by 2 and 2 divisions by 3.

import collections

def twoOperations(num):

    if num == 0: return 1
    stack = collections.deque([(1, 0)])
    visited = set([0])

    while stack:
        val, step = stack.popleft()

        if val == num:
            return step

        if val * 2 not in visited:
            visited.add(val * 2)
            stack.append((val * 2, step + 1))

        if val // 3 not in visited:
            visited.add(val // 3)
            stack.append((val // 3, step + 1))