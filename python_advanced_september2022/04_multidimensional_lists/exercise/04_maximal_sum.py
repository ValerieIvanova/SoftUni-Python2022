import sys

rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
submatrix = []
max_sum = -sys.maxsize
for row in range(rows - 2):
    for col in range(cols - 2):
        current_square = [
            list(map(int, [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]])),
            list(map(int, [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]])),
            list(map(int, [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]))
        ]

        current_sum = sum(sum(current_square, []))
        if current_sum > max_sum:
            max_sum = current_sum
            submatrix = current_square
print(f"Sum = {max_sum}")
for row in range(len(submatrix)):
    for col in range(len(submatrix[row])):
        print(submatrix[row][col], end=' ')
    print()