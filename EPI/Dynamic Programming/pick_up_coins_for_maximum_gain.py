# In the pick-up-coins game, an even number of coins are placed in a line. Two players take turns at choosing one coin each -- they can only choose grom the two coins a the end of the line. The game ends when all the coins have been picked up. They player whose coins have the higher total value wins. A player cannot pass his turn.

# Design an efficient algorithm for computing the maximum total value for the starting player in the pick-up-coins game.

# minmax
def maximumGain(arr):

    def traverse(arr, ismax):
        if len(arr) == 2: return max(arr)
        if ismax:
            return max(traverse(arr[:-1], ismax is False) + arr[-1], traverse(arr[1:], ismax is False) + arr[0])
        else:
            return min(traverse(arr[:-1], ismax is False), traverse(arr[1:], ismax is False))

    return traverse(arr, True)

# minmax with memoization
def maximumGain(arr):

    d = {}

    def traverse(a, b):
        if b < a: return 0
        if (a, b) in d: return d[a, b]

        option_1 = arr[a] + min(traverse(a + 1, b - 1), traverse(a + 2, b))
        option_2 = arr[b] + min(traverse(a + 1, b - 1), traverse(a, b - 2))

        d[a, b] = max(option_1, option_2)
        return d[a, b]
        

    return traverse(0, len(arr) - 1)