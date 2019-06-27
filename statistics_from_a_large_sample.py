# 1093. Statistics from a Large Sample
# User Accepted: 1762
# User Tried: 2195
# Total Accepted: 1786
# Total Submissions: 4831
# Difficulty: Medium
# We sampled integers between 0 and 255, and stored the results in an array count:  count[k] is the number of integers we sampled equal to k.

# Return the minimum, maximum, mean, median, and mode of the sample respectively, as an array of floating point numbers.  The mode is guaranteed to be unique.

# (Recall that the median of a sample is:

# The middle element, if the elements of the sample were sorted and the number of elements is odd;
# The average of the middle two elements, if the elements of the sample were sorted and the number of elements is even.)

# Constraints:

# count.length == 256
# 1 <= sum(count) <= 10^9
# The mode of the sample that count represents is unique.
# Answers within 10^-5 of the true value will be accepted as correct.

def sampleStats(nums):
        
    min_num = -1
    max_num = 0
    mean = 0
    median = 0
    mode = 0
    mode_num = 0
    count = 0
    
    total = sum(nums)
    
    for k, v in enumerate(nums):
        if v > 0:
            if min_num < 0:
                min_num = float(k)
                
            max_num = float(k)
            
            if mode_num < v:
                mode = float(k)
                mode_num = v
                
            mean += float(v) * k / total
            
            if total % 2 != 0:
                if count < total // 2 + 1 and count + v >= total // 2 + 1:
                    median = float(k)
            else:
                if count < total // 2 and count + v >= total // 2:
                    median = k
                elif count + v == total // 2:
                    median = k
                elif count == total // 2:
                    median = float(median + k) / 2
                
            count += v
            
    return [min_num, max_num, mean, median, mode]