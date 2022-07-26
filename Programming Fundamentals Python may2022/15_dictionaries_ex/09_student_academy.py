rows = int(input())
grades_dict = {}
for _ in range(rows):
    student = input()
    grade = float(input())
    if student not in grades_dict:
        grades_dict[student] = []
    grades_dict[student].append(grade)

[print(f"{student} -> {sum(grades)/len(grades):.2f}") for student, grades in grades_dict.items()
 if sum(grades)/len(grades) >= 4.5]
# For loop
# for student, grades in grades_dict.items():
#     if sum(grades) / len(grades) >= 4.5:
#         print(f"{student} -> {sum(grades)/len(grades):.2f}")