# number_of_poor_grades = int(input())
# number_of_problems = 0
# poor_grades_counter = 0
# average_grades = 0
# last_problem = ''
# problem_name = input()
# while problem_name != 'Enough':
#     grade = int(input())
#     average_grades += grade
#     number_of_problems += 1
#     last_problem = problem_name
#     problem_name = input()
#     if grade <= 4:
#         poor_grades_counter += 1
#         if poor_grades_counter >= number_of_poor_grades:
#             print(f'You need a break, {poor_grades_counter} poor grades.')
#             break
#         continue
# if problem_name == 'Enough':
#     average_grades /= number_of_problems
#     print(f'Average score: {average_grades:.2f}')
#     print(f'Number of problems: {number_of_problems}')
#     print(f'Last problem: {last_problem}')

# ----------------------------------------------------

number_of_poor_grades = int(input())
number_of_problems = 0
poor_grades_counter = 0
average_grades = 0
last_problem = ''
failed = False
while poor_grades_counter < number_of_poor_grades:
    problem_name = input()
    if problem_name == 'Enough':
        failed = True
        average_grades /= number_of_problems
        print(f'Average score: {average_grades:.2f}')
        print(f'Number of problems: {number_of_problems}')
        print(f'Last problem: {last_problem}')
        break
    grade = int(input())
    if grade <= 4:
        poor_grades_counter += 1
    average_grades += grade
    number_of_problems += 1
    last_problem = problem_name
if poor_grades_counter >= number_of_poor_grades:
    print(f'You need a break, {poor_grades_counter} poor grades.')