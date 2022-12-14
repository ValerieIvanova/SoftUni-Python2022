rows, cols = [int(x) for x in input().split()]
string = list(input())
matrix = []
idx = 0
for row in range(rows):
    res = ''
    for col in range(cols):
        res += string[idx % len(string)]
        idx += 1
    if row % 2 == 0:
        matrix.append(res)
    else:
        matrix.append(res[::-1])

[print(*snake, sep='') for snake in matrix]