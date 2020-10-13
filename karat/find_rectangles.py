# I just gave my phone interview after completing the OA, about a week ago. It was through a third party-Karat. I was asked to walk through my resume. Then some questions related to Systems Programming, Load Balancing, Stong consistency and eventual consistency, one question related to SQL commands out of nowhere. In the last 10 mins I was supposed to solve and test this question :
# /*
# Imagine we have an image. We'll represent this image as a simple 2D array where every pixel is a 1 or a 0.

# The image you get is known to have potentially many distinct rectangles of 0s on a background of 1's. Write a function that takes in the image and returns the coordinates of all the 0 rectangles -- top-left and bottom-right; or top-left, width and height.

# image1 = [
# [0, 1, 1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1, 1, 1],
# [0, 1, 1, 0, 0, 0, 1],
# [1, 0, 1, 0, 0, 0, 1],
# [1, 0, 1, 1, 1, 1, 1],
# [1, 0, 1, 0, 0, 1, 1],
# [1, 1, 1, 0, 0, 1, 1],
# [1, 1, 1, 1, 1, 1, 0],
# ]

# Sample output variations (only one is necessary):

# findRectangles(image1) =>
# // (using top-left-row-column and bottom-right):
# [
# [[0,0],[0,0]],
# [[2,0],[2,0]],
# [[2,3],[3,5]],
# [[3,1],[5,1]],
# [[5,3],[6,4]],
# [[7,6],[7,6]],
# ]
# // (using top-left-x-y and width/height):
# [
# [[0,0],[1,1]],
# [[0,2],[1,1]],
# [[3,2],[3,2]],
# [[1,3],[1,3]],
# [[3,5],[2,2]],
# [[6,7],[1,1]],
# ]

# Other test cases:

# image2 = [
# [0],
# ]

# findRectangles(image2) =>
# // (using top-left-row-column and bottom-right):
# [
# [[0,0],[0,0]],
# ]

# // (using top-left-x-y and width/height):
# [
# [[0,0],[1,1]],
# ]

# image3 = [
# [1],
# ]

# findRectangles(image3) => []

# image4 = [
# [1, 1, 1, 1, 1],
# [1, 0, 0, 0, 1],
# [1, 0, 0, 0, 1],
# [1, 0, 0, 0, 1],
# [1, 1, 1, 1, 1],
# ]

# findRectangles(image4) =>
# // (using top-left-row-column and bottom-right or top-left-x-y and width/height):
# [
# [[1,1],[3,3]],
# ]

# n: number of rows in the input image
# m: number of columns in the input image
# */

def find_rectangles(image):

    visited = set()

    def search(x, y):
        new_x, new_y = x, y
        for dx, dy in [[0, 1], [1, 0]]:
            if 0 <= x + dx < len(image) and 0 <= y + dy < len(image[0]) and (x + dx, y + dy) not in visited and image[x + dx][y + dy] == 0:
                visited.add((x + dx, y + dy))
                tx, ty = search(x + dx, y + dy)

                new_x = max(new_x, tx)
                new_y = max(new_y, ty)
        return new_x, new_y

    res = []
    for x in range(len(image)):
        for y in range(len(image[0])):
            if image[x][y] == 0 and (x, y) not in visited:
                bx, by = search(x, y)
                res.append([[x, y], [bx, by]])

    return res

image1 = [
[0, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 0, 0, 0, 1],
[1, 0, 1, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 1],
[1, 0, 1, 0, 0, 1, 1],
[1, 1, 1, 0, 0, 1, 1],
[1, 1, 1, 1, 1, 1, 0],
]

print(find_rectangles(image1))

image2 = [
[0],
]

print(find_rectangles(image2))