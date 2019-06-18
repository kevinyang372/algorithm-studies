# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def is_unique(inp):

    for i in range(len(inp) - 1):
        if inp[i] in inp[i + 1:]
            return False

    return True


# Right Answer:

def is_unique(inp):

    # this assumes all characters in the input are ascii
    if len(inp) > 128: return False

    char = [False for _ in range(128)]

    for i in inp:
        var = ord(i)
        if char[var]:
            return False
        char[var] = True

    return True
