from math import ceil
students = int(input())
lectures = int(input())
additional_bonus = int(input())
highest_bonus, highest_attendance = 0, 0
for student in range(students):
    attendance = int(input())
    total_bonus = attendance/lectures * (5 + additional_bonus)
    if total_bonus > highest_bonus:
        highest_bonus, highest_attendance = total_bonus, attendance
print(f'Max Bonus: {ceil(highest_bonus)}.\n'
      f'The student has attended {highest_attendance} lectures.')