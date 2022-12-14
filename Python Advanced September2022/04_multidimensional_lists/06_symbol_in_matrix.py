n = int(input())
matrix = []

for row in range(n):
    matrix.append(list(input()))

char = input()
position = None
for row in range(n):
    for col in range(n):
        if matrix[row][col] == char:
            position = (row, col)
            print(position)
            break
    if position:
        break

if not position:
    print(f"{char} does not occur in the matrix")