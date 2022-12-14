def captured(player, pos):
    r, c = pos[0], pos[1]
    opponent_init = players[0][0].lower()
    if player == 'w':
        if c > 0:
            if board[r - 1][c - 1] == opponent_init:
                return col_init[c - 1] + row_init[r - 1]
        if c + 1 < SIZE:
            if board[r - 1][c + 1] == opponent_init:
                return col_init[c + 1] + row_init[r - 1]

    elif player == 'b':
        if c + 1 < SIZE:
            if board[r + 1][c + 1] == opponent_init:
                return col_init[c + 1] + row_init[r + 1]
        if c > 0:
            if board[r + 1][c - 1] == opponent_init:
                return col_init[c - 1] + row_init[r + 1]


def promoted(player, pos):
    r, c = pos[0], pos[1]
    if player == 'b':
        if r + 1 == SIZE:
            return col_init[c] + row_init[r]
    elif player == 'w':
        if r - 1 < 0:
            return col_init[c] + row_init[r]


SIZE = 8
board = []

positions = {
    "w": [],
    "b": []
}

players = [
    'White',
    'Black'
]

directions = {
    "w": [-1, 0],
    "b": [1, 0]
}

for row in range(SIZE):
    line = input().split()
    if 'w' in line:
        positions["w"] = [row, line.index('w')]
    elif 'b' in line:
        positions["b"] = [row, line.index('b')]

    board.append(line)

row_init = {
    0: '8',
    1: '7',
    2: '6',
    3: '5',
    4: '4',
    5: '3',
    6: '2',
    7: '1',
}

col_init = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h',
}

while True:
    current_player = players.pop(0)
    current_player_init = current_player[0].lower()
    current_pos = positions[current_player_init]

    is_promoted = promoted(current_player_init, current_pos)
    if is_promoted:
        print(f"Game over! {current_player} pawn is promoted to a queen at {is_promoted}.")
        break

    is_captured = captured(current_player_init, current_pos)
    if is_captured:
        print(f"Game over! {current_player} win, capture on {is_captured}.")
        break

    board[current_pos[0]][current_pos[1]] = '-'
    positions[current_player_init][0] += directions[current_player_init][0]
    board[current_pos[0]][current_pos[1]] = current_player_init

    players.append(current_player)
