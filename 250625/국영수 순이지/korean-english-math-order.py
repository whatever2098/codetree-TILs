n = int(input())
name = []
korean = []
english = []
math = []

students = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))
    students.append((student_info[0], student_info[1], student_info[2], student_info[3]))

students.sort(key=lambda x:(-int(x[1]), -int(x[2]), -int(x[3])) )

for student in students:
    name, korean, english, math = student
    print(name, korean, english, math)

