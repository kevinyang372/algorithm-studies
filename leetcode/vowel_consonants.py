import collections

def solution(S):
    
    vowels = {'A', 'E', 'I', 'O', 'U'}
    
    def traverse(is_vowel, pool):
        if not pool['vowels'] and not pool['consonants']:
            return 1
        
        count = 0
        if is_vowel:
            if not pool['consonants']: return 0

            to_visit = list(pool['consonants'].keys())
            for char in to_visit:
                pool['consonants'][char] -= 1
                if pool['consonants'][char] == 0:
                    pool['consonants'].pop(char)
                count += traverse(not is_vowel, pool)
                pool['consonants'][char] += 1
        else:
            if not pool['vowels']: return 0

            to_visit = list(pool['vowels'].keys())
            for char in to_visit:
                pool['vowels'][char] -= 1
                if pool['vowels'][char] == 0:
                    pool['vowels'].pop(char)
                count += traverse(not is_vowel, pool)
                pool['vowels'][char] += 1
        
        return count
    
    temp = {}
    temp['vowels'] = collections.Counter(list(filter(lambda x: x in vowels, S)))
    temp['consonants'] = collections.Counter(list(filter(lambda x: x not in vowels, S)))
    
    return traverse(True, temp)