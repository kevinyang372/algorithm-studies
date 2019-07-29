# Your task is to write an algorithm to optimize the sets of forward/return shipping route pairs that allow the aircraft to be optimally utilized, given a list a of forward routes and a list of return shipping routes.

# INPUT
# The input to the function/method consisits of three arguments:
# maxTravelDist, an integer representing the maximum operating travel distance of the given aircraft;
# forwardRouteList, a list of pairs of integers where the first integer represents the unique identifier of a forward shipping
# route and the second integer represents the amount of travel distance required bu this shipping route;
# returnRouteList, a list of pairs of integers where the first integer represents the unique identifer of a return shipping route
# and the second integer represents the amount of travel distance required by this shipping route.

# OUTPUT
# Return a list of pairs of integers representing the pairs of IDs of forward and return shipping routes that optimally utilize the given aircraft. If no route is possible, return a list with empty pair.

# Example 1:
# Input:
# maxTravelDist = 7000
# forwardRouteList = [[1,2000],[2,4000],[3,6000]]
# returnRouteList = [[1,2000]]

# Output:
# [[2,1]]

# Explanation:
# There are only three combinations [1,1],[2,1],and [3,1], which have a total of 4000, 6000, and 8000 miles, respectively. Since 6000 is the largest use that does tnot exceed 7000, [2,1] is the optimal pair.

# Example 2:
# Input:
# maxTravelDist = 10,000
# forwardRouteList = [[1,3000],[2,5000],[3,7000],[4,10000]]
# returnRouteList = [[1,2000],[2,3000],[3,4000],[4,5000]]

# Output:
# [[2,4],[3,2]]

# Explanation:
# There are two pairs of forward and return shipping routes possible that optimally utilizes the given aircraft. Shipping Route ID#2 from the forwardShippingRouteList, required 5000 miles travelled, and Shipping Route ID#4 from returnShippingRouteList also required 5000 miles travelled. Combined, they add up to 10000 miles travelled. Similarily, Shipping Route ID#3 from forwardShippingRouteList requires 7000 miles travelled, and Shippping Route ID#2 from returnShippingRouteList requires 3000 miles travelled. These also add up to 10000 miles travelled. Therefore, the pairs of forward and return shipping routes that optimally utilize the aircraft are [2,4] and [3,2].

def optimalUtilization(maxTravelDist, forwardRouteList, returnRouteList):

    forwardRouteList = sorted(forwardRouteList, key = lambda x: x[1])
    returnRouteList = sorted(returnRouteList, key = lambda x: x[1])

    queue = [(0, len(returnRouteList) - 1)]
    res = []
    maximum = 0

    while queue:
        i, j = queue.pop(0)
        sums = forwardRouteList[i][1] + returnRouteList[j][1]

        if sums <= maxTravelDist:
            if maximum > sums:
                continue
            elif sums > maximum:
                maximum = sums
                res = [[forwardRouteList[i][0], returnRouteList[j][0]]]
            else:
                res.append([forwardRouteList[i][0], returnRouteList[j][0]])

            if i + 1 < len(forwardRouteList):
                queue.append((i + 1, j))
        else:
            if j - 1 >= 0:
                queue.append((i, j - 1))

    return res
