string = input()
size = int(input())

field = []
player_pos = []
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    line = list(input())
    if 'P' in line:
        player_pos = [row, line.index('P')]
        line[player_pos[1]] = '-'
    field.append(line)

M = int(input())

for i in range(M):
    command = input()
    field[player_pos[0]][player_pos[1]] = '-'
    row, col = player_pos[0] + directions[command][0], player_pos[1] + directions[command][1]
    if not 0 <= row < size or not 0 <= col < size:
        string = string[0:len(string)-1]
        field[player_pos[0]][player_pos[1]] = 'P'
        continue
    position = field[row][col]
    if position.isalpha():
        string += position
        field[row][col] = 'P'
    player_pos = [row, col]


print(string)
[print(*row, sep='') for row in field]