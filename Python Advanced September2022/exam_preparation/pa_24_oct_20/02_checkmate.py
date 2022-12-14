# SIZE = 8
# board = []
# king_pos = []
# queens_pos = []
# for row in range(SIZE):
#     line = input().split()
#     if 'K' in line:
#         king_pos = [row, line.index('K')]
#     board.append(line)
#
# # Diagonals:
# for i in range(SIZE):
#     row = king_pos[0] + i
#     col = king_pos[1] + i
#     if not 0 <= col < SIZE or not 0 <= row < SIZE:
#         break
#     if board[row][col] == 'Q':
#         queens_pos.append([row, col])
#         break
#
# for i in range(SIZE):
#     row = king_pos[0] + i
#     col = king_pos[1] - i
#     if not 0 <= col < SIZE or not 0 <= row < SIZE:
#         break
#     if board[row][col] == 'Q':
#         queens_pos.append([row, col])
#         break
#
# for i in range(SIZE):
#     row = king_pos[0] - i
#     col = king_pos[1] - i
#     if not 0 <= col < SIZE or not 0 <= row < SIZE:
#         break
#     if board[row][col] == 'Q':
#         queens_pos.append([row, col])
#         break
#
# for i in range(SIZE):
#     row = king_pos[0] - i
#     col = king_pos[1] + i
#     if not 0 <= col < SIZE or not 0 <= row < SIZE:
#         break
#     if board[row][col] == 'Q':
#         queens_pos.append([row, col])
#         break
#
# # Left
# for i in range(SIZE):
#     row = king_pos[0]
#     col = king_pos[1] - i
#     if not 0 <= col < SIZE:
#         break
#     if board[row][col] == 'Q':
#         queens_pos.append([row, col])
#         break
#
# # Right
# for i in range(SIZE):
#     row = king_pos[0]
#     col = king_pos[1] + i
#     if not 0 <= col < SIZE:
#         break
#     if board[row][col] == 'Q':
#         queens_pos.append([row, col])
#         break
#
# # Up
# for i in range(SIZE):
#     row = king_pos[0] - i
#     col = king_pos[1]
#     if not 0 <= row < SIZE:
#         break
#     if board[row][col] == 'Q':
#         queens_pos.append([row, col])
#         break
#
# # Down
# for i in range(SIZE):
#     row = king_pos[0] + i
#     col = king_pos[1]
#     if not 0 <= row < SIZE:
#         break
#     if board[row][col] == 'Q':
#         queens_pos.append([row, col])
#         break
#
# if queens_pos:
#     print(*queens_pos, sep='\n')
# else:
#     print('The king is safe!')


def check_valid_index(r, c):
    return 0 <= r < SIZE and 0 <= c < SIZE


def moves(r, c, direction):
    return r + directions[direction][0], c + directions[direction][1]


SIZE = 8
king_row, king_col, board, queens_pos = 0, 0, [], []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "top left diagonal": (-1, -1),
    "top right diagonal": (-1, 1),
    "bottom left diagonal": (1, -1),
    "bottom right diagonal": (1, 1),
}

for row in range(SIZE):
    board.append(input().split())
    if "K" in board[row]:
        king_row, king_col = row, board[row].index('K')

for direction in directions:
    new_row, new_col = king_row, king_col
    for steps in range(SIZE):
        new_row, new_col = moves(new_row, new_col, direction)
        if not check_valid_index(new_row, new_col):
            break
        if board[new_row][new_col] == 'Q':
            queens_pos.append([new_row, new_col])
            break

if queens_pos:
    print(*queens_pos, sep='\n')
else:
    print('The king is safe!')