# Implement a SnapshotArray that supports the following interface:

# SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
# void set(index, val) sets the element at the given index to be equal to val.
# int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
# int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
 

# Example 1:

# Input: ["SnapshotArray","set","snap","set","get"]
# [[3],[0,5],[],[0,6],[0,0]]
# Output: [null,null,0,null,5]
# Explanation: 
# SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
# snapshotArr.set(0,5);  // Set array[0] = 5
# snapshotArr.snap();  // Take a snapshot, return snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
 

# Constraints:

# 1 <= length <= 50000
# At most 50000 calls will be made to set, snap, and get.
# 0 <= index < length
# 0 <= snap_id < (the total number of times we call snap())
# 0 <= val <= 10^9

class SnapshotArray(object):

    def __init__(self, length):
        self.d = collections.defaultdict(list)
        self.version = 0
        
        for i in range(length):
            self.d[i].append((self.version, 0))
        

    def set(self, index, val):
        if self.d[index][-1][0] == self.version:
            self.d[index].pop()
        self.d[index].append((self.version, val))
        

    def snap(self):
        self.version += 1
        return self.version - 1
        

    def get(self, index, snap_id):
        ind = bisect.bisect_right(self.d[index], (snap_id, float('inf')))
        return self.d[index][ind - 1][1]