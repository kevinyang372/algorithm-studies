# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

# Each element is either an integer, or a list -- whose elements may also be integers or other lists.

# Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

# Example 1:

# Input: [[1,1],2,[1,1]]
# Output: 8 
# Explanation: Four 1's at depth 1, one 2 at depth 2.
# Example 2:

# Input: [1,[4,[6]]]
# Output: 17 
# Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.

def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        
    if not nestedList: return 0
    
    stack = collections.deque()
    
    for i in nestedList:
        stack.append((i, 1))
    
    d, maxDepth = collections.defaultdict(int), 1
    
    while stack:
        node, level = stack.popleft()
        maxDepth = max(maxDepth, level)
        
        if node.isInteger():
            d[level] += node.getInteger()
            continue
        
        for c in node.getList():
            stack.append((c, level + 1))
        
    res = 0
    for i in range(1, maxDepth + 1):
        res += d[i] * (maxDepth + 1 - i)
        
    return res