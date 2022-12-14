n = int(input())
matrix = []
for i in range(n):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)

# Diagonal top left to bottom right
sum_diagonal = 0
for index in range(n):
    sum_diagonal += matrix[index][index]
print(sum_diagonal)