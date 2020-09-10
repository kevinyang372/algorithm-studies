'''
Given a root interval node with children nodes, expand those nodes in order with non-overlapping intervals

Node:
    id: 1
    start: 0
    end: 100
    children: [2]

Node:
    id: 2
    start: 25
    end: 70
    children: []

(1, 0, 25)
(2, 25, 70)
(1, 70, 100)


---------
Node 1: (1, 0, 100, [2, 3])
Node 2: (2, 25, 40, [])
Node 3: (3, 50, 70, [])

(1, 0, 25)
(2, 25, 40)
(1, 40, 50)
(3, 50, 70)
(1, 70, 100)
'''

def expand_node(root):
    start_index = end_index = root.start
    result = []

    for child in root.children:
        end_index = child.start

        if start_index < end_index:
            result.append((root.id, start_index, end_index))

        result.extend(expand_node(child))
        start_index = child.end

    if start_index < root.end:
        result.append((root.id, start_index, root.end))
    
    return result

  
'''
stack = [(1, 0, 100, [2, 3])]
result = [(1, 0, 25)]

stack = [(1, 25, 100, [3]), (2, 25, 40, [])]
result = [(1, 0, 25), (2, 25, 40)]

stack = [(1, 70, 100, []), (3, 50, 70, [])]
'''
def expand_node_iterative(root):

    def expand(node):
        return [node.id, node.start, node.end, collections.deque(node.children)]

    stack = [expand(root)]
    result = []

    while stack:
        id, start_ind, end_ind, children = stack.pop()
        
        if not children:
            result.append((id, start_ind, end_ind))
            continue
        
        if start_ind < children[0].start:
            result.append((id, start_ind, children[0].start))

        child = expand(children.popleft())
        start_ind = child.end
        
        stack.append([id, start_ind, end_ind, children])
        stack.append(child)

    return result 