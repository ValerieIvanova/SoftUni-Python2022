from collections import deque

cups_capacity = deque(map(int, input().split()))  # queue
bottle_capacity = list(map(int, input().split()))  # stack
wasted_water = 0

while True:
    if not cups_capacity or not bottle_capacity:
        break
    bottle = bottle_capacity[-1]
    cup = cups_capacity[0]
    if cup <= bottle:
        wasted_water += bottle_capacity.pop() - cups_capacity.popleft()
    elif cup > bottle:
        cups_capacity[0] -= bottle_capacity.pop()
if not cups_capacity:
    print(f"Bottles: {' '.join(str(b) for b in bottle_capacity)}")
elif not bottle_capacity:
    print(f"Cups: {' '.join(str(c) for c in cups_capacity)}")
print(f"Wasted litters of water: {wasted_water}")