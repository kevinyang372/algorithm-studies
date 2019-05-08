# Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

# Example 1:

# Input: num = "123", target = 6
# Output: ["1+2+3", "1*2*3"] 
# Example 2:

# Input: num = "232", target = 8
# Output: ["2*3+2", "2+3*2"]
# Example 3:

# Input: num = "105", target = 5
# Output: ["1*0+5","10-5"]
# Example 4:

# Input: num = "00", target = 0
# Output: ["0+0", "0-0", "0*0"]
# Example 5:

# Input: num = "3456237490", target = 9191
# Output: []

def divide_into_numbers(num):

    if len(num) == 2:
        return [[num[0], num[1]], [num]]

    result = []

    top = num[0]
    without_top = divide_into_numbers(num[1:])

    for i in without_top:

        temp = i[:]
        temp[0] = top + temp[0]
        result.append(temp)

        result.append([top] + i)

    bottom = num[-1]
    without_bottom = divide_into_numbers(num[:-1])

    for i in without_bottom:

        temp = i[:]
        temp[-1] = temp[-1] + bottom
        result.append(temp)

        result.append(i + [bottom])

    result = sorted(result)
    result = [result[i] for i in range(len(result)) if i == 0 or result[i] != result[i-1]]

    return result

def calculate(nums):

    if len(nums) == 1:
        return [int(nums[0])]

    origin = int(nums[0])
    res = calculate(nums[1:])

    result = []
    for i in res:
        result.append(origin + i)
        result.append(origin * i)
        result.append(origin - i)

    return result

def expression_add_operators(nums, target):

    expression_list = divide_into_numbers(nums)
    sums = 0

    for i in expression_list:
        temp = calculate(i)
        sums += sum([1 for t in temp if t == target])

    return sums
