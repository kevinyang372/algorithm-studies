# The count-and-say sequence is the sequence of integers with the first five terms as following:

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221

# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.

# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

# Note: Each term of the sequence of integers will be represented as a string.

def count_and_say(n):

    if n == 1:
        return 1

    res = count_and_say(n-1)

    if res < 10:
        return int('1%s' % res)

    start = res % 10
    count = 1
    end = ''

    res = res // 10

    while res >= 1:

        temp = res % 10

        if temp == start:
            count += 1
        else:
            end = int("%s%s%s" % (count, start, end))
            count = 1
            start = temp

        res = res // 10

    end = int("%s%s%s" % (count, start, end))

    return end