# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

# Each element is either an integer, or a list -- whose elements may also be integers or other lists.

# Example 1:

# Input: [[1,1],2,[1,1]]
# Output: 10 
# Explanation: Four 1's at depth 2, one 2 at depth 1.
# Example 2:

# Input: [1,[4,[6]]]
# Output: 27 
# Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.

def depthSum(self, nestedList: List[NestedInteger]) -> int:
    stack = [(i, 1) for i in nestedList]
    sums = 0

    while stack:
        node, level = stack.pop()
        
        if node.isInteger():
            sums += node.getInteger() * level
        else:
            for t in node.getList():
                stack.append((t, level + 1))

    return sums
            