from math import ceil
number_of_people = int(input())
capacity_of_the_elevator = int(input())
courses = 0
# courses = 0 if elevator_capacity == 0 else ceil(number_of_people / capacity_of_the_elevator)
if capacity_of_the_elevator != 0:
    courses = ceil(number_of_people / capacity_of_the_elevator)
print(courses)