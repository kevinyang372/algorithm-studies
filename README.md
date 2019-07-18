# Elements of Programming Interviews in Python

## Arrays

### Time Complexities
* Retrieval and update - O(1)
* Insertion (with resizing) - O(1)
* Deletion (moving all successive elements to the left) - O(N)
* Slicing - O(k) k is the slice size

### Key Functions
* `bisect.bisect`: find a position in list where an element needs to be inserted to keep the list sorted
```python
import bisect
a = [1,2,3,5]
bisect.bisect(a, 4)
# returns 3
```
* How copy works: <br>
  __shallow copy__: constructing a new collection object and then populating it with references to the child objects found in the original <br>
  __deep copy__: first constructing a new collection object and then recursively populating it with copies of the child objects found in the original
```python
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs) # shallow

xs[1][0] = 'X'
print(ys) # [[1, 2, 3], ['X', 5, 6], [7, 8, 9]]

import copy
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = copy.deepcopy(xs) # deep

print(ys) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
* List comprehension with multiple levels of looping
```python
A = [1,3,5]
B = ['A','B','C']
[(x, y) for x in A for y in B]
```

### Tips
* Filing an array from the front is slower than from behind (append)
* Overwritting is more time efficient than deleting

## Strings

### Time Complexities
Strings are immutable
* Concatenating a single character - O(N)

### Key Functions
* `s.strip()`: remove the starting and ending empty spaces
* `s.startswith(prefix)` and `s.endswith(suffix)`
* `s.tolower()`

## Linked Lists

### Time Complexities
* Insertion and deletion - O(1)
* Obtaining the kth element - O(N)

### Tips
* Use a _dummy head_ (with null value) to avoid having to check for empty lists
* Algorithms on linked lists usually benefit from using two iterators with one move faster than the other

