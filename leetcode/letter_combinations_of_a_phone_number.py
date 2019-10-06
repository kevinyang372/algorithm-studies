# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

def letterCombinations(digits):

    if len(digits) == 0: return []

    dic = {'1':[], 
        '2':['a', 'b', 'c'],
        '3':['d', 'e', 'f'],
        '4':['g', 'h', 'i'],
        '5':['j', 'k', 'l'],
        '6':['m', 'n', 'o'],
        '7':['p', 'q', 'r', 's'],
        '8':['t', 'u', 'v'],
        '9':['w', 'x', 'y', 'z'],
        '0':[' ']}

    t = digits[0]
    
    if len(digits) == 1:
        return dic[t]
    
    res = self.letterCombinations(digits[1:])
    fin = []

    for m in dic[t]:
        for n in res:
            fin.append(m + n)

    return fin