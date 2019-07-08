# You have a stack of n boxes, with widths Wi' heights hi' and depths d • The boxes
# 1
# cannot be rotated and can only be stacked on top of one another if each box in the stack is strictly larger than the box above it in width, height. and depth. Implement a method to compute the height of the tallest possible stack. The height of a stack is the sum of the heights of each box.

def stack(boxes):

    if not boxes: return 0
    if len(boxes) == 1: return boxes[0][1]

    p = sorted(boxes, key = lambda x: (x[0], x[1], x[2]))[::-1]

    h1 = 0

    for t in range(1, len(p)):
        if p[t][0] < p[0][0] and p[t][1] < p[0][1] and p[t][2] < p[0][2]:
            h1 = max(stack(boxes[t:]) + p[0][1], h1)

    return max(h1, stack(boxes[1:]))