# Question:
# You are on a flight and wanna watch two movies during this flight.
# You are given int[] movie_duration which includes all the movie durations.
# You are also given the duration of the flight which is d in minutes.
# Now, you need to pick two movies and the total duration of the two movies is less than or equal to (d - 30min).
# Find the pair of movies with the longest total duration. If multiple found, return the pair with the longest movie.

# Example 1:

# Input: movie_duration = [90, 85, 75, 60, 120, 150, 125], d = 250
# Output: [90, 125]
# Explanation: 90min + 125min = 215 is the maximum number within 220 (250min - 30min)

def movieDuration(dur, d):

    if d < 30: return []
    d -= 30
    dur = sorted(dur)

    i, j = 0, len(dur) - 1
    max_dur = 0
    res = []

    while i <= j:
        sums = dur[i] + dur[j]
        if sums > d:
            j -= 1
        else:
            if sums > max_dur:
                max_dur = sums
                res = [dur[i], dur[j]]  
            elif sums == max_dur:
                if max(dur[i], dur[j]) > max(res):
                    res = [dur[i], dur[j]]
                    j -= 1
            i += 1

    return res




