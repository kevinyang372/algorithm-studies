# Design a queue that supports push and pop operations in the front, middle, and back.

# Implement the FrontMiddleBack class:

# FrontMiddleBack() Initializes the queue.
# void pushFront(int val) Adds val to the front of the queue.
# void pushMiddle(int val) Adds val to the middle of the queue.
# void pushBack(int val) Adds val to the back of the queue.
# int popFront() Removes the front element of the queue and returns it. If the queue is empty, return -1.
# int popMiddle() Removes the middle element of the queue and returns it. If the queue is empty, return -1.
# int popBack() Removes the back element of the queue and returns it. If the queue is empty, return -1.
# Notice that when there are two middle position choices, the operation is performed on the frontmost middle position choice. For example:

# Pushing 6 into the middle of [1, 2, 3, 4, 5] results in [1, 2, 6, 3, 4, 5].
# Popping the middle from [1, 2, 3, 4, 5, 6] returns 3 and results in [1, 2, 4, 5, 6].
 

# Example 1:

# Input:
# ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
# [[], [1], [2], [3], [4], [], [], [], [], []]
# Output:
# [null, null, null, null, null, 1, 3, 4, 2, -1]

# Explanation:
# FrontMiddleBackQueue q = new FrontMiddleBackQueue();
# q.pushFront(1);   // [1]
# q.pushBack(2);    // [1, 2]
# q.pushMiddle(3);  // [1, 3, 2]
# q.pushMiddle(4);  // [1, 4, 3, 2]
# q.popFront();     // return 1 -> [4, 3, 2]
# q.popMiddle();    // return 3 -> [4, 2]
# q.popMiddle();    // return 4 -> [2]
# q.popBack();      // return 2 -> []
# q.popFront();     // return -1 -> [] (The queue is empty)
 

# Constraints:

# 1 <= val <= 109
# At most 1000 calls will be made to pushFront, pushMiddle, pushBack, popFront, popMiddle, and popBack.

# Optimal - two deques
class FrontMiddleBackQueue:

    def __init__(self):
        self.first_queue = collections.deque()
        self.second_queue = collections.deque()
        
    def rebalanceQueue(self) -> None:
        len_f1, len_f2 = len(self.first_queue), len(self.second_queue)
        
        if len_f1 == len_f2 or len_f1 == len_f2 - 1:
            return
        elif len_f1 > len_f2:
            self.second_queue.appendleft(self.first_queue.pop())
        elif len_f1 < len_f2 - 1:
            self.first_queue.append(self.second_queue.popleft())

    def pushFront(self, val: int) -> None:
        self.first_queue.appendleft(val)
        self.rebalanceQueue()

    def pushMiddle(self, val: int) -> None:
        self.first_queue.append(val)
        self.rebalanceQueue()

    def pushBack(self, val: int) -> None:
        self.second_queue.append(val)
        self.rebalanceQueue()

    def popFront(self) -> int:
        if len(self.second_queue) == 0: return -1
        if len(self.first_queue) == 0:
            val = self.second_queue.popleft()
        else:
            val = self.first_queue.popleft()
        self.rebalanceQueue()
        return val

    def popMiddle(self) -> int:
        if len(self.second_queue) == 0: return -1
        
        if len(self.first_queue) == len(self.second_queue):
            val = self.first_queue.pop()
        else:
            val = self.second_queue.popleft()
            
        self.rebalanceQueue()
        return val

    def popBack(self) -> int:
        if len(self.second_queue) == 0: return -1
        val = self.second_queue.pop()
        self.rebalanceQueue()
        return val

# Linked List approach
class DoublyLinkedNode:
    
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None

        
class FrontMiddleBackQueue:

    def __init__(self):
        self.size = 0
        self.DUMMY_HEAD = DoublyLinkedNode('DUMMAY_HEAD')
        self.DUMMY_TAIL = DoublyLinkedNode('DUMMAY_TAIL')
        
        self.DUMMY_HEAD.next, self.DUMMY_TAIL.prev = self.DUMMY_TAIL, self.DUMMY_HEAD
        
    def insertBefore(self, node, to_insert) -> None:
        prev_node = node.prev
        prev_node.next, to_insert.prev = to_insert, prev_node
        to_insert.next, node.prev = node, to_insert
        
    def detachNode(self, node) -> None:
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node

    def pushFront(self, val: int) -> None:
        new_node = DoublyLinkedNode(val)
        self.insertBefore(self.DUMMY_HEAD.next, new_node)
        self.size += 1

    def pushMiddle(self, val: int) -> None:
        pos = self.size // 2
        new_node = DoublyLinkedNode(val)
        node = self.DUMMY_HEAD
        
        for _ in range(pos):
            node = node.next
        
        self.insertBefore(node.next, new_node)
        self.size += 1

    def pushBack(self, val: int) -> None:
        new_node = DoublyLinkedNode(val)
        self.insertBefore(self.DUMMY_TAIL, new_node)
        self.size += 1

    def popFront(self) -> int:
        if self.size == 0: return -1
        node = self.DUMMY_HEAD.next
        
        self.detachNode(node)
        self.size -= 1
        return node.val

    def popMiddle(self) -> int:
        if self.size == 0: return -1
        pos = (self.size - 1) // 2
        
        node = self.DUMMY_HEAD.next
        for _ in range(pos):
            node = node.next
        
        self.detachNode(node)
        self.size -= 1
        return node.val

    def popBack(self) -> int:
        if self.size == 0: return -1
        node = self.DUMMY_TAIL.prev
        
        self.detachNode(node)
        self.size -= 1
        return node.val