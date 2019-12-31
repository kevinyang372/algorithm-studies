# You are given a string a_{cat,dog}_is_with_{sarah,mike}
# Return the outputs as:
# a_cat_is_with_sarah
# a_cat_is_with_mike
# a_dog_is_with_sarah
# a_dog_is_with_mike

def braceExpansion(s):

    if '{' not in s: return [s]

    i = s.index('{')
    t = s.index('}')

    choices = s[i + 1: t].split(',')
    res, temp = [], braceExpansion(s[t + 1:])

    for n in choices:
        for m in temp:
            res.append(s[:i] + n + m)

    return res

def expand(self, S):
        
    if not S: return ['']
    
    pre = ''
    for ind, char in enumerate(S):
        if char == '{':
            temp = ind + 1
            lis, opt = [], ''
            while temp < len(S) and S[temp] != "}":
                if S[temp] == ',':
                    lis.append(opt)
                    opt = ''
                else:
                    opt += S[temp]
                temp += 1
            
            if opt: lis.append(opt)
            
            res, fin = [], self.expand(S[temp + 1:])
            
            for opt in sorted(lis):
                for lat in fin:
                    res.append(pre + opt + lat)
            
            return res
        else:
            pre += char
    
    return [pre]