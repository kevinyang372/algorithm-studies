# Design a data structure that supports all following operations in average O(1) time.

# Note: Duplicate elements are allowed.
# insert(val): Inserts an item val to the collection.
# remove(val): Removes an item val from the collection if present.
# getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.
# Example:

# // Init an empty collection.
# RandomizedCollection collection = new RandomizedCollection();

# // Inserts 1 to the collection. Returns true as the collection did not contain 1.
# collection.insert(1);

# // Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
# collection.insert(1);

# // Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
# collection.insert(2);

# // getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
# collection.getRandom();

# // Removes 1 from the collection, returns true. Collection now contains [1,2].
# collection.remove(1);

# // getRandom should return 1 and 2 both equally likely.
# collection.getRandom();

class RandomizedCollection(object):

    def __init__(self):
        self.c = collections.Counter()
        self.d = {}
        self.list = []
        

    def insert(self, val):
        
        if val in self.c:
            res = False
        else:
            res = True
        
        self.c[val] += 1
        self.d["%s_%s" % (val, self.c[val])] = len(self.list)
        self.list.append((val, self.c[val]))
        
        return res
        

    def remove(self, val):
        if self.c[val] < 1:
            return False
        else:
            current = "%s_%s" % (val, self.c[val])
            last = "%s_%s" % (self.list[-1][0], self.list[-1][1])
            self.d[last] = self.d[current]
            self.list[self.d[current]] = self.list[-1]
            self.list.pop()
            self.c[val] -= 1
            del self.d[current]
            return True
    
    def getRandom(self):
        return random.choice(self.list)[0]