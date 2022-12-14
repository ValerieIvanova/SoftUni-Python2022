size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]
primary_diagonal = 0
secondary_diagonal = 0
for i in range(size):
    primary_diagonal += matrix[i][i]
    secondary_diagonal += matrix[i][-1-i]
print(abs(primary_diagonal-secondary_diagonal))