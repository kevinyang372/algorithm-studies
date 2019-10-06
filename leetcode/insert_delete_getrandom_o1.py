# Design a data structure that supports all following operations in average O(1) time.

# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
# Example:

# // Init an empty set.
# RandomizedSet randomSet = new RandomizedSet();

# // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomSet.insert(1);

# // Returns false as 2 does not exist in the set.
# randomSet.remove(2);

# // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomSet.insert(2);

# // getRandom should return either 1 or 2 randomly.
# randomSet.getRandom();

# // Removes 1 from the set, returns true. Set now contains [2].
# randomSet.remove(1);

# // 2 was already in the set, so return false.
# randomSet.insert(2);

# // Since 2 is the only number in the set, getRandom always return 2.
# randomSet.getRandom();

# unoptimized
class RandomizedSet(object):

    def __init__(self):
        self.inputs = []
        

    def insert(self, val):
        if val not in self.inputs:
            self.inputs.append(val)
            return True
        return False
        

    def remove(self, val):
        if val in self.inputs:
            self.inputs.pop(self.inputs.index(val))
            return True
        return False
    

    def getRandom(self):
        return self.inputs[random.randint(0, len(self.inputs) - 1)]

#optimized insert and remove
class RandomizedSet(object):

    def __init__(self):
        self.inputs, self.pos = [], {}
        

    def insert(self, val):
        if val not in self.inputs:
            self.pos[val] = len(self.inputs)
            self.inputs.append(val)
            return True
        return False
        

    def remove(self, val):
        if val in self.pos:
            pos = self.pos[val]
            last = self.inputs[-1]
            self.pos[last] = pos
            self.inputs[pos] = last
            self.inputs.pop()
            self.pos.pop(val, 0)
            return True
        return False
    

    def getRandom(self):
        return self.inputs[random.randint(0, len(self.inputs) - 1)]

