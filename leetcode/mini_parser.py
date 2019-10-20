# Given a nested list of integers represented as a string, implement a parser to deserialize it.

# Each element is either an integer, or a list -- whose elements may also be integers or other lists.

# Note: You may assume that the string is well-formed:

# String is non-empty.
# String does not contain white spaces.
# String contains only digits 0-9, [, - ,, ].
# Example 1:

# Given s = "324",

# You should return a NestedInteger object which contains a single integer 324.
# Example 2:

# Given s = "[123,[456,[789]]]",

# Return a NestedInteger object containing a nested list with 2 elements:

# 1. An integer containing value 123.
# 2. A nested list containing two elements:
#     i.  An integer containing value 456.
#     ii. A nested list with one element:
#          a. An integer containing value 789.

def deserialize(self, s):
        
    if s[0] != '[': return NestedInteger(int(s.split(',')[0]))
    
    stack = []
    i = 0
    curr = ''
    
    while i < len(s) - 1:
        if s[i] == '[':
            stack.append(NestedInteger())
        elif s[i] == ']':
            if curr != '':
                stack[-1].add(NestedInteger(int(curr)))
                curr = ''
                
            pre = stack.pop()
            val = stack[-1].getInteger()
            
            if val:
                stack[-1].add(NestedInteger(val))
                
            stack[-1].add(pre)
        elif s[i] == ',':
            if curr != '':
                stack[-1].add(NestedInteger(int(curr)))
                curr = ''
        else:
            curr += s[i]
        i += 1
    
    if curr:
        stack[-1].add(NestedInteger(int(curr)))
    
    return stack[-1]