# Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

# Note:
# The number of people is less than 1,100.

 
# Example

# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

# TLE
def reconstructQueue(self, people):
    if len(people) < 2: return people
    
    min_val = float('inf')
    for x, y in people:
        if y == 0:
            min_val = min(min_val, x)
            
    new_people = []
    for x, y in people:
        if x == min_val and y == 0:
            continue
        elif x <= min_val:
            new_people.append([x, y - 1])
        else:
            new_people.append([x, y])
    
    res = self.reconstructQueue(new_people)
    for i, v in enumerate(res):
        if v[0] <= min_val:
            res[i][1] += 1
    
    return [[min_val, 0]] + res

# heap
def reconstructQueue(self, people):
    if len(people) < 2: return people
    
    q = [[y, x, 0] for x, y in people]
    heapq.heapify(q)
    res = []
    
    while q:
        c, n, delta = heapq.heappop(q)
        res.append([n, c + delta])
        
        for ind, (x, y, d) in enumerate(q):
            if y <= n:
                q[ind] = [x - 1, y, d + 1]
                
        heapq.heapify(q)
    
    return res