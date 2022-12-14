from collections import deque

petrol_pumps = int(input())
queue = deque()

for _ in range(petrol_pumps):
    data = [int(x) for x in input().split()]
    queue.append(data)

for position in range(petrol_pumps):
    tank = 0
    failed = False
    for fuel, distance in queue:
        tank += fuel
        if distance > tank:
            failed = True
            break
        else:
            tank -= distance
    if failed:
        queue.append(queue.popleft())   # queue.rotate(-1)
    else:
        print(position)
        break