# Given array of sentences, return the set of words that are in one sentence but not all.

# For example:

# "My dog eats food"
# "She eats food too"
# "My dog food is good good"

# Would return ['She', 'too', 'is', 'good']

def wordSet(sentences):
    if not sentences: return

    pool, visited = set(), set()
    for i in sentences:
        temp = set(i.split(' '))
        diff = temp.intersection(pool)
        pool.update(temp)
        pool -= diff
        visited.update(diff)

    return list(pool - visited)