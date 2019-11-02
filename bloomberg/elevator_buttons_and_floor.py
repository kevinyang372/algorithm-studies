# Elevator has two buttons Up and Down , By pressing up elevator goes up by p floors and by pressing down it goes down by q floors. A building has n floors. Given a starting floor s, Can you explain if it's possible to go to floor e.

def canReach(start, target, up, down, total):
    dp = [False] * total
    stack = [start]

    while stack:
        node = stack.pop()

        if dp[node]:
            continue
        elif node == target:
            return True
        else:
            dp[node] = True
            if node + up < total + 1:
                stack.append(node + up)
            if node - down > 0:
                stack.append(node - down)

    return False