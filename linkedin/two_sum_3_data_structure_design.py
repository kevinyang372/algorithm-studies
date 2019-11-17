# Design and implement a TwoSum class. It should support the following operations: add and find.

# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.

# Example 1:

# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false
# Example 2:

# add(3); add(1); add(2);
# find(3) -> true
# find(6) -> false

# TLE
class TwoSum:

    def __init__(self):
        self.sums = set()
        self.val = []
        

    def add(self, number: int) -> None:
        if self.val:
            for i in self.val:
                self.sums.add(i + number)
        self.val.append(number)
        

    def find(self, value: int) -> bool:
        return value in self.sums

class TwoSum:

    def __init__(self):
        self.sums = {}
        

    def add(self, number: int) -> None:
        self.sums[number] = number in self.sums
        

    def find(self, value: int) -> bool:
        return any((value - i != i and value - i in self.sums) or (value - i == i and self.sums[i]) for i in self.sums)