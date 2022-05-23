number_of_jury = int(input())
students_counter = 0
total_grades = 0

while True:
    current_grade_for_student_presentation = 0
    name_of_presentation = input()
    if name_of_presentation == 'Finish':
        total_grades = total_grades / (number_of_jury * students_counter)
        print(f"Student's final assessment is {total_grades:.2f}.")
        break
    students_counter += 1
    for _ in range(number_of_jury):
        member_jury_grade = float(input())
        current_grade_for_student_presentation += member_jury_grade
        total_grades += member_jury_grade
    current_grade_for_student_presentation /= number_of_jury
    print(f'{name_of_presentation} - {current_grade_for_student_presentation:.2f}.')
