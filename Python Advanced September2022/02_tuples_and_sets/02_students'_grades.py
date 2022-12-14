n = int(input())
grades_dict = {}

for i in range(n):
    student, grade = input().split()
    if student not in grades_dict:
        grades_dict[student] = []
    grades_dict[student].append(float(grade))

for student, grades in grades_dict.items():
    avr_grade = sum(grades) / len(grades)
    unpacked_grades = ' '.join(str(f"{x:.2f}") for x in grades)
    print(f"{student} -> {unpacked_grades} (avg: {avr_grade:.2f})")