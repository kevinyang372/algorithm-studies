# Write a method to return all subsets of a set.

def powerSet(num):
    if len(num) == 1: return [[num[0]],[]]

    powerset = powerSet(num[1:])
    return powerset + [i + [num[0]] for i in powerset]
