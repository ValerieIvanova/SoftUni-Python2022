lines = int(input())
cars_set = set()
for i in range(lines):
    direction, car_number = input().split(', ')
    if direction == 'IN':
        cars_set.add(car_number)
    else:
        cars_set.remove(car_number)

if not cars_set:
    print('Parking Lot is Empty')
else:
    [print(car) for car in cars_set]