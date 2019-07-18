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

# TLE
def addOperators(self, num, target):
    if not num: return
    
    d = [num[0]]
    res = set()
    
    for i in range(1, len(num)):
        temp = []
        for t in d:
            for sig in ["", "+", "-", "*"]:
                if sig == "" and t[-1] == '0' and (len(t) < 2 or not t[-2].isdigit()):
                    continue
                if i < len(num) - 1:
                    temp.append("%s%s%s" % (t, sig, num[i]))
                    
                if num[i] != '0' or i == len(num) - 1:
                    tes = "%s%s%s" % (t, sig, num[i:])
                    if eval(tes) == target:
                        res.add(tes)
        d = temp
    
    return list(res)