projection = input()
rows = int(input())
columns = int(input())

income = 0

cinema_capacity = rows * columns
if projection == 'Premiere':
     income = cinema_capacity * 12
elif projection == 'Normal':
     income = cinema_capacity * 7.50
elif projection == 'Discount':
     income = cinema_capacity * 5

print(f'{income:.2f} leva')