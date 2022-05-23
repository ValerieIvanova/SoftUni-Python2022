# from math import ceil
#
# h_of_the_wall = int(input())
# w_of_the_wall = int(input())
# percent_no_paint_area = int(input())
# area = h_of_the_wall * w_of_the_wall * 4
# painting_area = ceil(area - (area * (percent_no_paint_area / 100)))
# painting = painting_area
# is_tired = False
# while painting <= painting_area:
#     command = input()
#     if command == 'Tired!':
#         is_tired = True
#         break
#     paint_liters = int(command)
#     painting -= paint_liters
#     if painting <= 0:
#         break
# if is_tired:
#     print(f"{painting} quadratic m left." )
# elif painting >= 0:
#     print(f"All walls are painted! Great job, Pesho!")
# else:
#     print(f"All walls are painted and you have {abs(painting)} l paint left!")

import math

height = int(input())
width = int(input())
percent = int(input())
total_space = height * width * 4
total_paint = math.ceil(total_space - (total_space * (percent / 100)))
counter = 0
while counter < total_paint:
    litters = input()
    if litters == "Tired!":
        break
    litters = int(litters)
    counter += litters
    if counter == total_paint:
        break
diff = abs(counter - total_paint)
if counter > total_paint:
    print(f"All walls are painted and you have {diff} l paint left!")
elif counter == total_paint:
    print(f"All walls are painted! Great job, Pesho!")
else:
    print(f"{diff} quadratic m left.")