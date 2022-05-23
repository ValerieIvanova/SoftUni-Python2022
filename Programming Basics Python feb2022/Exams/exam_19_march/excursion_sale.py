sea_trips = int(input())
mountain_trips = int(input())
profit = 0
while True:
    package_name = input()
    if package_name == 'Stop':
        break
    if package_name == 'sea':
        if sea_trips == 0:
            continue
        profit += 680
        sea_trips -= 1
    elif package_name == 'mountain':
        if mountain_trips == 0:
            continue
        profit += 499
        mountain_trips -= 1
    if sea_trips == 0 and mountain_trips == 0:
        print("Good job! Everything is sold.")
        break
print(f'Profit: {profit} leva.')