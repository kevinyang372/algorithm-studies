# Given a collection of actions and userIds an error occurs when a userId takes a specific action in order for example

# A => B => => C gives an errror
# B => A => C no error and etc

# Write a function that takes in a list of (Actions, UserIds) pairs and returns the user Id that ecounters the error

# Sample Input:

# action_user_1 = [
# ["A", "1"],
# ["B", "1"],
# ["B", "2"],
# ["C", "1"],
# ["C", "2"],
# ["C", "3"],
# ["A", "2],
# ["A", "3"],
# ["A", "2"],
# ["B", "2],
# ["C", "2"],
# ]

# Expected output 1,2

# action_user_2 = [
# ["A", "1"],
# ["A", "1"]
# ["A", "1"]
# ["B", "1"],
# ["B", "2"],
# ["C", "2"],
# ["C", "2"],
# ["C", "3"],
# ["A", "2],
# ["A", "3"],
# ["A", "2"],
# ["B", "2],
# ["C", "2"],
# ]

# Expected output 2

import collections

def get_errored_users(error_seq, actions):

    d = collections.defaultdict(list)
    res = set()

    for action, user_id in actions:
        curr_progress = d.get(user_id, [0])
        temp = []

        for i in range(len(curr_progress)):
            if error_seq[curr_progress[i]] == action:
                updated = curr_progress[i] + 1
                if updated == len(error_seq):
                    res.add(user_id)
                else:
                    temp.append(updated)

        if action == error_seq[0]:
            temp.append(1)

        d[user_id] = temp

    return list(res)

action_user_1 = [
["A", "1"],
["B", "1"],
["B", "2"],
["C", "1"],
["C", "2"],
["C", "3"],
["A", "2"],
["A", "3"],
["A", "2"],
["B", "2"],
["C", "2"],
]

error_seq = ["A", "B", "C"]
print(get_errored_users(error_seq, action_user_1))