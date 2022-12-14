from collections import deque

caffeine = deque(int(x) for x in input().split(', '))
energy_drinks = deque(int(x) for x in input().split(', '))
max_caffeine = 300
total_caffeine = 0

while caffeine and energy_drinks:
    current_caffeine_mg = caffeine.pop()
    current_nrg_drink = energy_drinks.popleft()
    result = current_caffeine_mg * current_nrg_drink

    if result <= max_caffeine:
        total_caffeine += result
        max_caffeine -= result

    elif result > max_caffeine:
        energy_drinks.append(current_nrg_drink)
        if total_caffeine - 30 >= 0:
            total_caffeine -= 30
            max_caffeine += 30
        else:
            max_caffeine += total_caffeine
            total_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")