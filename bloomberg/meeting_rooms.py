# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

# For example,

# Given [[0, 30],[5, 10],[15, 20]],
# return false.

def meetingRooms(arr):
    arr.sort()

    for i in range(1, len(arr)):
        if arr[i][0] < arr[i - 1][1]
            return False

    return True