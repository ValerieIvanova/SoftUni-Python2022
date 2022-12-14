rows, columns = [int(x) for x in input().split(', ')]
matrix = []
for _ in range(rows):
    elements = [int(x) for x in input().split(', ')]
    matrix.append(elements)

max_sum = -999999999999999
max_sub_matrix = []
for row in range(rows-1):  # rows - 1 За да избегнем index error
    for col in range(columns-1):
        sub_matrix = [matrix[row][col],
                      matrix[row][col+1],
                      matrix[row+1][col],
                      matrix[row+1][col+1]]
        current_sum = sum(sub_matrix)
        if current_sum > max_sum:
            max_sum = current_sum
            max_sub_matrix = sub_matrix.copy()
print(max_sub_matrix[0], max_sub_matrix[1])
print(max_sub_matrix[2], max_sub_matrix[3])
print(max_sum)