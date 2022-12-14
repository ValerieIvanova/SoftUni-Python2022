SIZE = 6
board = [input().split() for _ in range(SIZE)]

total_points = 0
for _ in range(3):
    row, col = map(int, input().strip('()').split(', '))
    if 0 <= row < SIZE and 0 <= col < SIZE:
        if board[row][col] == 'B':
            board[row][col] = 'X'
            for r in range(SIZE):
                for _ in range(1):
                    c = col
                    if board[r][c].isdigit():
                        total_points += int(board[r][c])

if total_points >= 300:
    print(f"Good job! You scored {total_points} points, and you've won Lego Construction Set.")
elif 200 <= total_points <= 299:
    print(f"Good job! You scored {total_points} points, and you've won Teddy Bear.")
elif 100 <= total_points <= 199:
    print(f"Good job! You scored {total_points} points, and you've won Football.")
else:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")