rows = int(input())
matrix = [input().split(', ') for _ in range(rows)]
primary_diagonal = []
secondary_diagonal = []

for i in range(rows):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][-1 - i])

print(f"Primary diagonal: {', '.join(primary_diagonal)}. Sum: {sum(map(int, primary_diagonal))}\n"
      f"Secondary diagonal: {', '.join(secondary_diagonal)}. Sum: {sum(map(int, secondary_diagonal))}")
