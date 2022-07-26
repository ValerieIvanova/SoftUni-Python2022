# students = {}
#
# while True:
#     student_data = input()
#     if ":" in student_data:
#         name, ID, course = student_data.split(":")
#         students[ID] = name, course
#     else:
#         current_course = student_data.replace('_', ' ')
#         break
# for id, data in students.items():
#     if current_course in data:
#         print(f'{data[0]} - {id}')

courses = {}

while True:
    student_data = input()
    if ":" in student_data:
        name, id, course = student_data.split(':')
        if course not in courses:
            courses[course] = {}
        courses[course][id] = name
    else:
        searched_course = student_data.replace('_', ' ')
        break

for course_name in courses:
    if course_name == searched_course:
        for id, name in courses[course_name].items():
            print(f'{name} - {id}')