courses_dict = {}
while True:
    command = input()
    if command == 'end':
        break
    course_name, student_name = command.split(' : ')
    if course_name not in courses_dict:
        courses_dict[course_name] = [student_name]
    else:
        courses_dict[course_name].append(student_name)

for course in courses_dict:
    print(f"{course}: {len(courses_dict[course])}")
    [print(f"-- {student}") for student in courses_dict[course]]