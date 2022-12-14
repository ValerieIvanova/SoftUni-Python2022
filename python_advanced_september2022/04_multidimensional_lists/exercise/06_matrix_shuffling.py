rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

while True:
    command = input()
    if command == 'END':
        break
    command = command.split()
    if command[0] == 'swap' and len(command[1:]) == 4:
        row1, col1, row2, col2 = [int(x) for x in command[1:]]
        if False not in [0 <= row1 < len(matrix),
                         0 <= row2 < len(matrix),
                         0 <= col1 < len(matrix[0]),
                         0 <= col2 < len(matrix[0])
                         ]:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            [print(*matrix[row]) for row in range(rows)]
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
