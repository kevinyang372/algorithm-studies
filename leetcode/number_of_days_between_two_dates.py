# Write a program to count the number of days between two dates.

# The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

 

# Example 1:

# Input: date1 = "2019-06-29", date2 = "2019-06-30"
# Output: 1
# Example 2:

# Input: date1 = "2020-01-15", date2 = "2019-12-31"
# Output: 15
 

# Constraints:

# The given dates are valid dates between the years 1971 and 2100.

def daysBetweenDates(self, date1: str, date2: str) -> int:
        
    if date1 > date2:
        date1, date2 = date2, date1
    
    m2d = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    
    y1, m1, d1 = map(int, date1.split('-'))
    y2, m2, d2 = map(int, date2.split('-'))
    d = 0
    
    while y1 <= y2 or m1 <= m2:
        
        if m1 == 2 and y1 % 4 == 0 and (y1 % 100 != 0 or y1 % 400 == 0):
            month = m2d[m1] + 1
        else:
            month = m2d[m1]
        
        if y1 == y2 and m1 == m2:
            d += d2 - d1
            break
        elif d1 != 1:
            d += month - d1 + 1
            m1 += 1
            d1 = 1
        else:
            d += month
            m1 += 1
        
        if m1 == 13:
            y1 += 1
            m1 = 1
    
    return d