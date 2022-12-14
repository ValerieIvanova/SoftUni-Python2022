rows = int(input())
# matrix = []
# for i in range(rows):
#     elements = [int(el) for el in input().split(', ') if int(el) % 2 == 0]

matrix = [[int(el) for el in input().split(', ') if int(el) % 2 == 0] for _ in range(rows)]
print(matrix)