rows, columns = map(int, input().split(', '))
matrix = []
total_sum = 0
for _ in range(rows):
    elements = list(map(int, input().split(', ')))
    matrix.append(elements)
    total_sum += sum(elements)
print(total_sum)
print(matrix)