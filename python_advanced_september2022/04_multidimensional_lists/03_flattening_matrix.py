rows = int(input())
matrix = []

for _ in range(rows):
    elements = input().split(', ')
    matrix.append([int(x) for x in elements])
flattened_matrix = [num for row in matrix for num in row]
print(flattened_matrix)

# Getting the matrix flattened with For Loop:
# flattened_matrix = []
# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         flattened_matrix.append(matrix[row][col])

# With Extend method:
# for _ in range(rows):
#     elements = input().split(', ')
#     matrix.extend([int(x) for x in elements])
# print(matrix)

