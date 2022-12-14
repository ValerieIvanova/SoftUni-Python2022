def coordinates(pos, direction_):
    current_row, current_col = pos[0], pos[1]
    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }
    row = current_row + directions[direction_][0]
    col = current_col + directions[direction_][1]
    return row, col


def create(pos, direction_, val, matrix_):
    r, c = coordinates(pos, direction_)
    if matrix_[r][c] == '.':
        matrix_[r][c] = val
    pos = (r, c)
    return matrix_, pos


def update(pos, direction_, val, matrix_):
    r, c = coordinates(pos, direction_)
    if matrix_[r][c] != '.':
        matrix_[r][c] = val
    pos = (r, c)
    return matrix_, pos


def delete(pos, direction_, matrix_):
    r, c = coordinates(pos, direction_)
    if matrix_[r][c] != '.':
        matrix_[r][c] = '.'
    pos = (r, c)
    return matrix_, pos


def read(pos, direction_):
    r, c = coordinates(pos, direction_)
    if matrix[r][c] != '.':
        print(matrix[r][c])
    pos = (r, c)
    return pos


size = 6
matrix = [input().split() for _ in range(size)]
my_pos = eval(input())

while True:
    command = input().split(', ')
    command_name = command[0]
    if command_name == 'Stop':
        break
    elif command_name == 'Create':
        direction, value = command[1:]
        matrix, my_pos = create(my_pos, direction, value, matrix)
    elif command_name == 'Update':
        direction, value = command[1:]
        matrix, my_pos = update(my_pos, direction, value, matrix)
    elif command_name == 'Delete':
        direction = command[1]
        matrix, my_pos = delete(my_pos, direction, matrix)
    elif command_name == 'Read':
        direction = command[1]
        my_pos = read(my_pos, direction)

[print(*row) for row in matrix]