lines = int(input())
capacity = 255
tank = 0
for i in range(lines):
    liters_of_water = int(input())
    if liters_of_water > capacity:
        print('Insufficient capacity!')
        continue
    tank += liters_of_water
    capacity -= liters_of_water
print(tank)