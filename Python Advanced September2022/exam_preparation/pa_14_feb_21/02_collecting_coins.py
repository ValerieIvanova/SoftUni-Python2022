from math import floor


def move(pos, command_):
    row, col = pos[0], pos[1]
    if command_ == 'up':
        row -= 1
    elif command_ == 'down':
        row += 1
    elif command_ == 'left':
        col -= 1
    elif command_ == 'right':
        col += 1
    if row < 0:
        row = size - 1
    elif row >= size:
        row = 0
    if col < 0:
        col = size - 1
    elif col >= size:
        col = 0

    return [row, col]


size = int(input())

field = []
player_coords = []
coins = 0

for r in range(size):
    line = input().split()
    if 'P' in line:
        player_coords = [r, line.index('P')]
    field.append(line)

path = [player_coords, ]

win = False

while True:
    command = input()
    player_coords = move(player_coords, command)
    path.append(player_coords)

    position = field[player_coords[0]][player_coords[1]]

    if position == 'X':
        coins //= 2
        break
    elif position.isdigit():
        coins += int(position)
        field[player_coords[0]][player_coords[1]] = 'P'
        if coins >= 100:
            win = True
            print(f"You won! You've collected {floor(coins)} coins.")
            break

if not win:
    print(f"Game over! You've collected {floor(coins)} coins.")
print('Your path:')
for c in path:
    print(c)
