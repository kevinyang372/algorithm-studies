# Given two numbers, hour and minutes. Return the smaller angle (in sexagesimal units) formed between the hour and the minute hand.

 

# Example 1:



# Input: hour = 12, minutes = 30
# Output: 165
# Example 2:



# Input: hour = 3, minutes = 30
# Output: 75
# Example 3:



# Input: hour = 3, minutes = 15
# Output: 7.5
# Example 4:

# Input: hour = 4, minutes = 50
# Output: 155
# Example 5:

# Input: hour = 12, minutes = 0
# Output: 0
 

# Constraints:

# 1 <= hour <= 12
# 0 <= minutes <= 59
# Answers within 10^-5 of the actual value will be accepted as correct.

def angleClock(self, hour: int, minutes: int) -> float:
        
    minute_to_angle = lambda x: x * 6
    hour_to_angle = lambda x, y: x * 30 + 0.5 * y
    
    return min(abs(minute_to_angle(minutes) - hour_to_angle(hour, minutes)), 360 - abs(minute_to_angle(minutes) -  hour_to_angle(hour, minutes)))