# We have a sequence of books: the i-th book has thickness books[i][0] and height books[i][1].

# We want to place these books in order onto bookcase shelves that have total width shelf_width.

# We choose some of the books to place on this shelf (such that the sum of their thickness is <= shelf_width), then build another level of shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down.  We repeat this process until there are no more books to place.

# Note again that at each step of the above process, the order of the books we place is the same order as the given sequence of books.  For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.

# Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.

 

# Example 1:


# Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
# Output: 6
# Explanation:
# The sum of the heights of the 3 shelves are 1 + 3 + 2 = 6.
# Notice that book number 2 does not have to be on the first shelf.
 

# Constraints:

# 1 <= books.length <= 1000
# 1 <= books[i][0] <= shelf_width <= 1000
# 1 <= books[i][1] <= 1000

# naive recursion O(2^n)
def minHeightShelves(books, shelf_width, cur_width = 0, cur_max = 0):
    if not books: return cur_max
    if books[0][0] + cur_width <= shelf_width:
        h = max(books[0][1], cur_max)

        if cur_width == 0:
            return minHeightShelves(books[1:], shelf_width, cur_width + books[0][0], h)
        else:
            return min(minHeightShelves(books[1:], shelf_width, cur_width + books[0][0], h), cur_max + minHeightShelves(books[1:], shelf_width, books[0][0], books[0][1]))
    else:
        return cur_max + minHeightShelves(books[1:], shelf_width, books[0][0], books[0][1])

# dp O(N)
def minHeightShelves(self, books, shelf_width):

    d = [float('inf')] * len(books)
    d[0] = books[0][1]

    for i in range(1, len(books)):
        sums = books[i][0]
        height = books[i][1]
        d[i] = height + d[i - 1]
        for j in range(i - 1, -1, -1):
            sums += books[j][0]
            height = max(books[j][1], height)
            if sums > shelf_width:
                break
            if j > 0:
                d[i] = min(d[i], d[j - 1] + height)
            else:
                d[i] = min(d[i], height)

    return d[-1]

