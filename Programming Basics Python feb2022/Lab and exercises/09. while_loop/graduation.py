name = input()
counter_grades = 0
bad_grades = 0
total_grades = 0
excluded = False
while counter_grades < 12:
    current_grade = float(input())
    if current_grade < 4:
        bad_grades += 1
        if bad_grades == 1:
            continue
        else:
            excluded = True
            counter_grades += 1
            print(f'{name} has been excluded at {counter_grades} grade')
            break
    total_grades += current_grade
    counter_grades += 1
if not excluded:
    avr_grade = total_grades / counter_grades
    print(f'{name} graduated. Average grade: {avr_grade:.2f}')