# Implement a MyCalendarTwo class to store your events. A new event can be added if adding the event will not cause a triple booking.

# Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

# A triple booking happens when three events have some non-empty intersection (ie., there is some time that is common to all 3 events.)

# For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.

# Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
# Example 1:

# MyCalendar();
# MyCalendar.book(10, 20); // returns true
# MyCalendar.book(50, 60); // returns true
# MyCalendar.book(10, 40); // returns true
# MyCalendar.book(5, 15); // returns false
# MyCalendar.book(5, 10); // returns true
# MyCalendar.book(25, 55); // returns true
# Explanation: 
# The first two events can be booked.  The third event can be double booked.
# The fourth event (5, 15) can't be booked, because it would result in a triple booking.
# The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
# The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
# the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
 

# Note:

# The number of calls to MyCalendar.book per test case will be at most 1000.
# In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].

class MyCalendarTwo(object):

    def __init__(self):
        self.events = []
        self.intersections = []

    def book(self, start, end):
        if not self.events: 
            self.events.append([start, end])
            return True
            
        insert_id = len(self.events)
        add_to_intersection = []
        
        for i, v in enumerate(self.events):
            if v[1] <= start:
                continue
            if v[0] >= end:
                insert_id = min(i, insert_id)
                break
            temp = self.check_intersection([start, end], v)
            add_to_intersection.append(temp)
            if not temp:
                return False
            elif start < v[0]:
                insert_id = min(i, insert_id)
            else:
                insert_id = min(i + 1, insert_id)
        
        self.events.insert(insert_id, [start, end])
        self.intersections += add_to_intersection
        return True
        
    def check_intersection(self, i1, i2, num = 0):
        if i1[1] <= i2[0] or i1[0] >= i2[1]:
            return True
        
        if num == 1: return False
        
        intersection = [max(i1[0], i2[0]), min(i1[1], i2[1])]
        
        for k in self.intersections:
            if not self.check_intersection(k, intersection, 1):
                return False
        
        return intersection