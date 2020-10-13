# Suppose we have an unsorted log file of accesses to web resources. Each log entry consists of an access time, the ID of the user making the access, and the resource ID.

# The access time is represented as seconds since 00:00:00, and all times are assumed to be in the same day.

# For example:
# logs = [
# ["58523", "user_1", "resource_1"],
# ["62314", "user_2", "resource_2"],
# ["54001", "user_1", "resource_3"],
# ["200", "user_6", "resource_5"],
# ["215", "user_6", "resource_4"],
# ["54060", "user_2", "resource_3"],
# ["53760", "user_3", "resource_3"],
# ["58522", "user_4", "resource_1"],
# ["53651", "user_5", "resource_3"],
# ["2", "user_6", "resource_1"],
# ["100", "user_6", "resource_6"],
# ["400", "user_7", "resource_2"],
# ["100", "user_8", "resource_2"],
# ["54359", "user_1", "resource_3"],
# ]

# Write a function that takes the logs and returns the resource with the highest number of accesses in any 5 minute window, together with how many accesses it saw.
# Example:
# ('resource_3', 3)

import collections

def find_highest_number_of_accesses(logs):

    logs.sort(key=lambda x: int(x[0]))

    d = collections.defaultdict(collections.deque)
    max_access = (-1, -1)

    for time, _, resource_id in logs:
        time = int(time)
        while d[resource_id] and time - d[resource_id][0] > 300:
            d[resource_id].popleft()
        d[resource_id].append(time)

        if len(d[resource_id]) > max_access[1]:
            max_access = (resource_id, len(d[resource_id]))

    return max_access


logs = [
["58523", "user_1", "resource_1"],
["62314", "user_2", "resource_2"],
["54001", "user_1", "resource_3"],
["200", "user_6", "resource_5"],
["215", "user_6", "resource_4"],
["54060", "user_2", "resource_3"],
["53760", "user_3", "resource_3"],
["58522", "user_4", "resource_1"],
["53651", "user_5", "resource_3"],
["2", "user_6", "resource_1"],
["100", "user_6", "resource_6"],
["400", "user_7", "resource_2"],
["100", "user_8", "resource_2"],
["54359", "user_1", "resource_3"],
]

print(find_highest_number_of_accesses(logs))
