# Given two arrays, write a function to compute their intersection.

def intersect(num1, num2):

    if len(num1) < 1:
        return ""
    elif num1 in num2:
        return num1
    else:
        rec1 = intersect(num1[1:], num2)
        print(num1, ":", rec1)
        if rec1 != "":
            return rec1
        
        rec2 = intersect(num1[:-1], num2)
        print(num1, ":", rec2)
        if rec2 != "":
            return rec2

    return ""

