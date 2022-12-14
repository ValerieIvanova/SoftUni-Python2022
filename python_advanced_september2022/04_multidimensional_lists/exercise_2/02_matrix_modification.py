rows = int(input())
matrix = [list(map(int, input().split())) for _ in range(rows)]

while True:
    command = input()
    if 'END' in command:
        [print(*row) for row in matrix]
        break

    row, col, value = [int(x) for x in command.split()[1:]]
    if False in [0 <= row < len(matrix), 0 <= col < len(matrix[0])]:
        print('Invalid coordinates')
        continue

    if 'Add' in command:
        matrix[row][col] += value
    elif 'Subtract' in command:
        matrix[row][col] -= value
