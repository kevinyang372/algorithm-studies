# You are a developer for a university. Your current project is to develop a system for students to find courses they share with friends. The university has a system for querying courses students are enrolled in, returned as a list of (ID, course) pairs.

# Write a function that takes in a list of (student ID number, course name) pairs and returns, for every pair of students, a list of all courses they share.

# Sample Input:

# student_course_pairs_1 = [
# ["58", "Linear Algebra"],
# ["94", "Art History"],
# ["94", "Operating Systems"],
# ["17", "Software Design"],
# ["58", "Mechanics"],
# ["58", "Economics"],
# ["17", "Linear Algebra"],
# ["17", "Political Science"],
# ["94", "Economics"],
# ["25", "Economics"],
# ["58", "Software Design"],
# ]

# Sample Output (pseudocode, in any order):

# find_pairs(student_course_pairs_1) =>
# {
# [58, 17]: ["Software Design", "Linear Algebra"]
# [58, 94]: ["Economics"]
# [58, 25]: ["Economics"]
# [94, 25]: ["Economics"]
# [17, 94]: []
# [17, 25]: []
# }

# Additional test cases:

# Sample Input:

# student_course_pairs_2 = [
# ["42", "Software Design"],
# ["0", "Advanced Mechanics"],
# ["9", "Art History"],
# ]

# Sample output:

# find_pairs(student_course_pairs_2) =>
# {
# [0, 42]: []
# [0, 9]: []
# [9, 42]: []
# }

# n: number of pairs in the input
# s: number of students
# c: number of courses being offered

import collections

def find_course_intersections(student_course_pairs):

    d = collections.defaultdict(set)

    for student_id, course in student_course_pairs:
        d[student_id].add(course)

    students = list(d.keys())
    result = collections.defaultdict(list)

    for i in range(len(students) - 1):
        for j in range(i + 1, len(students)):
            s1, s2 = students[i], students[j]
            result[s1, s2] = list(d[s1].intersection(d[s2]))

    return result

student_course_pairs_1 = [
    ["58", "Linear Algebra"],
    ["94", "Art History"],
    ["94", "Operating Systems"],
    ["17", "Software Design"],
    ["58", "Mechanics"],
    ["58", "Economics"],
    ["17", "Linear Algebra"],
    ["17", "Political Science"],
    ["94", "Economics"],
    ["25", "Economics"],
    ["58", "Software Design"],
]

print(find_course_intersections(student_course_pairs_1))
