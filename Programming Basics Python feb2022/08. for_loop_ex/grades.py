number_of_students = int(input())
a = 0
b = 0
c = 0
d = 0
total_grades = 0
for i in range(number_of_students):
    grade = float(input())
    if 2 <= grade <= 2.99:
        d += 1
        total_grades += grade
    elif 3 <= grade <= 3.99:
        c += 1
        total_grades += grade
    elif 4 <= grade <= 4.99:
        b += 1
        total_grades += grade
    elif grade >= 5:
        a += 1
        total_grades += grade
a_students = a / number_of_students * 100
b_students = b / number_of_students * 100
c_students = c / number_of_students * 100
d_students = d / number_of_students * 100
avrg_grades = total_grades / number_of_students
print(f'Top students: {a_students:.2f}%')
print(f'Between 4.00 and 4.99: {b_students:.2f}%')
print(f'Between 3.00 and 3.99: {c_students:.2f}%')
print(f'Fail: {d_students:.2f}%')
print(f'Average: {avrg_grades:.2f}')