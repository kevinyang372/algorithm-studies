# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# For example,

# Given [[0, 30],[5, 10],[15, 20]],
# return 2.

def meetingRoom(arr):
    arr.sort()
    rooms = []

    for i in arr:
        if not rooms:
            rooms.append(i[1])
        else:
            if i[0] <= rooms[-1]:
                ind = bisect.bisect_left(rooms, i[0])
                rooms[ind] = i[1]

                while ind < len(rooms) - 1 and rooms[ind] > rooms[ind + 1]:
                    rooms[ind], rooms[ind + 1] = rooms[ind + 1], rooms[ind]
                    ind += 1
            else:
                rooms.append(i[1])

    return len(rooms)