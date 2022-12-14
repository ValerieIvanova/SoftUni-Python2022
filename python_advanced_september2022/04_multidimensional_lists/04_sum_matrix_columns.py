rows, columns = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    elements = [int(x) for x in input().split()]
    matrix.append(elements)

# iterating through the columns
for col in range(columns):
    col_sum = 0
    for row in range(rows):
        col_sum += matrix[row][col]
    print(col_sum)