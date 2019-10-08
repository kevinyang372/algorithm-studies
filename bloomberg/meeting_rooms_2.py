# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# For example,

# Given [[0, 30],[5, 10],[15, 20]],
# return 2.

def minMeetingRooms(self, arr):
    arr.sort()
    rooms = []

    for i in arr:
        if not rooms:
            rooms.append(i[1])
        else:
            ind = bisect.bisect_right(rooms, i[0])
            
            if ind == 0:
                t = bisect.bisect_right(rooms, i[1])
                rooms.insert(t, i[1])
            else:
                rooms[ind - 1] = i[1]
                while ind < len(rooms) and rooms[ind - 1] > rooms[ind]:
                    rooms[ind - 1], rooms[ind] = rooms[ind], rooms[ind - 1]
                    ind += 1

    return len(rooms)