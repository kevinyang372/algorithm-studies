# Consider a vector of employees with a name and their title:
# [<John, Manager>, <Sally, CTO>, <Sam, CEO>, <Drax, Engineer>, <Bob, CFO>, <Daniel, Engineer>]

# And a dictionary where the keys report to the values:
# {[CTO, CEO], [Manager, CTO], [Engineer, Manager], [CFO, CEO]}

# Re-order the vector of employees according to the dictionary mappings. The vector of employees can be extremely big, however the dictionary only contains the title orderings.

# Sample output:
# [<Drax, Engineer>, <Daniel, Engineer>, <John, Manager>, <Sally, CTO>, <Bob, CFO>, <Sam, CEO>]

# Note that in this case, CTO and CFO both report to CEO so they are both before CEO and above the next biggest thing, which is manager. They can also be in either order in this case

import collections

def reorderArray(employees, order):

    graph = collections.defaultdict(list)
    degree = collections.Counter()

    for x, y in order:
        graph[x].append(y)
        degree[y] += 1

    d = collections.defaultdict(list)
    for name, rank in employees:
        d[rank].append(name)

    q = [(max([degree[i] for i in graph[y]], default = 0), y) for y in graph if degree[y] == 0]
    heapq.heapify(q)
    res = []

    while q:
        _, node = heapq.heappop(q)

        res += [(x, node) for x in d[node]]
        for neighbor in graph[node]:
            degree[neighbor] -= 1
            if degree[neighbor] == 0:
                heapq.heappush(q, (max([degree[i] for i in graph[neighbor]], default = 0), neighbor))

    return res