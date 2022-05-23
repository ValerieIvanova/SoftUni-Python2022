x = float(input())
y = float(input())
h = float(input())

side_wall_area = x * y
window_area = 1.5 * 1.5
both_side_walls = (2 * side_wall_area) - (2 * window_area)
back_wall = x * x
door = 1.2 * 2
front_and_back_wall_area = 2 * back_wall - door

total_area = both_side_walls + front_and_back_wall_area
green_paint = total_area / 3.4

both_roof_sides = 2 * (x * y)
both_triangles = 2 * (x * h / 2)
total_roof_area = both_roof_sides + both_triangles
red_paint = total_roof_area / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')
