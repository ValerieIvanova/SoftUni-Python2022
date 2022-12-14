SIZE = 6
field = []
pos = []

for row in range(SIZE):
    line = input().split()
    if 'E' in line:
        pos = [row, line.index('E')]

    field.append(line)

commands = input().split(', ')

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

deposits = {
    'W': [0, 'Water'],
    'M': [0, 'Metal'],
    'C': [0, 'Concrete']
}

for command in commands:
    pos[0] += directions[command][0]
    pos[1] += directions[command][1]
    if pos[0] < 0:
        pos[0] = SIZE - 1
    elif pos[0] == SIZE:
        pos[0] = 0
    if pos[1] < 0:
        pos[1] = SIZE - 1
    elif pos[1] == SIZE:
        pos[1] = 0

    rover_pos = field[pos[0]][pos[1]]

    if rover_pos in deposits:
        deposits[rover_pos][0] += 1
        print(f"{deposits[rover_pos][1]} deposit found at ({pos[0]}, {pos[1]})")
    elif rover_pos == 'R':
        print(f"Rover got broken at ({pos[0]}, {pos[1]})")
        break

if all([deposits['W'][0], deposits['C'][0], deposits['M'][0]]):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")