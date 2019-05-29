# Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

# Example 1:

# Input: "2-1-1"
# Output: [0, 2]
# Explanation: 
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# Example 2:

# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation: 
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10

def diffWaysToCompute(input):

    oper = ['+', '-', '*']

    min_p = len(input)
    max_p = 0

    for i in range(len(input)):
        if input[i] in oper:
            if i > max_p:
                max_p = i
            if i < min_p:
                min_p = i

    if min_p == max_p or max_p == 0:
        return [eval(input)]

    result = []
    result.append(eval(input))

    result += [eval("%s%s" % (input[:min_p + 1], i)) for i in diffWaysToCompute(input[min_p + 1:])]
    result += [eval("%s%s" % (i, input[max_p:])) for i in diffWaysToCompute(input[:max_p])]

    return result

