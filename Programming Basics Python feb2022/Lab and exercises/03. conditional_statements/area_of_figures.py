from math import pi
area = 0

figure = (input())

if figure == 'square':
    a = float(input())
    area = a * a

elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b

elif figure == 'circle':
    r = float(input())
    area = pi * r ** 2

elif figure == 'triangle':
    a = float(input())
    h = float(input())
    area = a * h / 2

print(f'{area:.3f}')
