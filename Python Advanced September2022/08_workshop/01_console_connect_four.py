# class InvalidColumnError(Exception):
#     pass
#
#
# def print_matrix(m):
#     [print(el) for el in m]
#
#
# def validate_col(col, max_cols):
#     if not (0 <= col <= max_cols):
#         raise InvalidColumnError
#     return False
#
#
# # Creating the matrix
# rows = 6
# cols = 7
# matrix = [[0 for _ in range(cols)] for _ in range(rows)]
#
# # Print current state
# print_matrix(matrix)
#
# player_num = 1
# while True:
#     player_num = 2 if player_num % 2 == 0 else 1
#     try:
#         # Read column choice from input and verify if the number is correct
#         column_num = int(input(f"Player {player_num}, please choose a column: ")) - 1
#         validate_col(column_num, cols - 1)
#     except InvalidColumnError:
#         print(f"This column is not valid. Please select a "
#               f"number between {1} and {cols}")
#         continue
#     except ValueError:
#         print(f"Please select a valid digit!")
#         continue
#     player_num += 1
#     print_matrix(matrix)

from collections import deque


def place_circle(row=0):
    if row == rows - 1 or board[row + 1][player_col] != '0':
        board[row][player_col] = player_symbol
        return
    place_circle(row + 1)


player_one_symbol = '1'
player_two_symbol = '2'

rows, cols = 6, 7

turn = deque([[1, player_one_symbol], [2, player_two_symbol]])
board = [['0'] * cols for _ in range(rows)]

directions = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (-1, -1),
    (1, 1),
    (-1, 1),
    (1, -1)
)

while True:
    [print(f"[ {', '.join(row)} ]") for row in board]
    player_number, player_symbol = turn[0]

    try:
        player_col = int(input(f"\nPlayer {player_number} please choose a column: ")) - 1
    except ValueError:
        print('Select a valid number')
        continue

    if not 0 <= player_col < cols:
        print(f"Select a valid number in the range ({1} - {cols})")
        continue

    row = 0
    if board[row][player_col] != '0':
        print('No empty spaces on that row')
        continue
    place_circle()

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == player_symbol:
                continue

            for coordinates in directions:
                r, c = row, col
                for _ in range(3):  # 3 is the number of iterations we need to check if the player wins.
                    r, c = r + coordinates[0], c + coordinates[1]

                    if not (0 <= r < rows and 0 <= c < cols):
                        break
                    if board[r][c] != player_symbol:
                        break
                else:
                    [print(f"[ {', '.join(row)} ]") for row in board]
                    print(f"The winner is player: {player_number}")
                    raise SystemExit

    turn.append(turn.popleft())
