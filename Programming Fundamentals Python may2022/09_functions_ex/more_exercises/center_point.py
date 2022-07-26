from math import floor


def closest_point(x1, y1, x2, y2):
    x, y = 0, 0
    if abs(x1) + abs(y1) <= abs(x2) + abs(y2):
        x, y = x1, y1
    elif abs(x2) + abs(y2) <= abs(x1) + abs(y1):
        x, y = x2, y2
    return f'({floor(x)}, {floor(y)})'


current_x1 = float(input())
current_y1 = float(input())
current_x2 = float(input())
current_y2 = float(input())
print(closest_point(current_x1, current_y1, current_x2, current_y2))