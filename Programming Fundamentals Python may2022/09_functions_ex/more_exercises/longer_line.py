from math import floor


def length(_x1, _y1, _x2, _y2):
    return (_x2 - _x1)**2 + (_y2 - _y1)**2


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
xx1 = float(input())
yy1 = float(input())
xx2 = float(input())
yy2 = float(input())
x1y1 = length(x1, y1, 0, 0)
x2y2 = length(x2, y2, 0, 0)
xx1yy1 = length(xx1, yy1, 0, 0)
xx2yy2 = length(xx2, yy2, 0, 0)
first_line = x1y1 + x2y2
second_line = xx1yy1 + xx2yy2
if first_line >= second_line:
    if x1y1 <= x2y2:
        print(f'({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})')
    else:
        print(f'({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})')
elif second_line >= first_line:
    if xx1yy1 <= xx2yy2:
        print(f'({floor(xx1)}, {floor(yy1)})({floor(xx2)}, {floor(yy2)})')
    else:
        print(f'({floor(xx2)}, {floor(yy2)})({floor(xx1)}, {floor(yy1)})')