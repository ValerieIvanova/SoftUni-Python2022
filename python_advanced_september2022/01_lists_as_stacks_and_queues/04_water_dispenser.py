from collections import deque

water_quantity = int(input())
queue = deque()
while True:
    command = input()
    if command == 'Start':
        break
    queue.append(command)

while True:
    command = input()
    if command == 'End':
        print(f"{water_quantity} liters left")
        break
    elif command.isdigit():
        liters = int(command)
        person = queue.popleft()
        if liters > water_quantity:
            print(f'{person} must wait')
        else:
            water_quantity -= liters
            print(f"{person} got water")
    elif command.startswith('refill'):
        liters = int(command.split()[1])
        water_quantity += liters
