# A permutation is a rearrangement of members of a sequence into a new sequence. For example, there are 24 permutations of <a, b, c, d>;

# A permutation can be specified by an array P, where P[i] represents the location of the element at i in the permutation. For example, the array <2, 0, 1, 3> represents the permutation that maps the element at location 0 to location 2, the element at location 1 to location 0, the element at location 2 to location 1, and keep the element at location 3 unchanged.

# For example, the permutation <2, 0, 1, 3> applied to A = <a, b, c, d> yields the array <b, c, a, d>. Given an array A of n elements and a permutation P, apply P to A

# O(N) time O(N) space
def permute(arr, p):
    d = {p[i]: arr[i] for i in range(len(arr))}
    return [d[i] for i in range(len(arr))]

# Circular approach
# O(N) time O(1) space
def permute(arr, p):
    for i in range(len(arr)):
        temp = i
        while p[temp] >= 0:
            arr[temp], arr[p[temp]] = arr[p[temp]], arr[temp]
            temp, p[temp] = p[temp], p[temp] - len(p)

    return arr
