def is_inside(r, c):
    if 0 <= r < size and 0 <= c < size:
        return True


def alive(r, c):
    if matrix[r][c] > 0:
        return True


def explosions(damage, m):
    if is_inside(row - 1, col) and alive(row - 1, col):
        m[row - 1][col] -= damage  # up
    if is_inside(row + 1, col) and alive(row + 1, col):
        m[row + 1][col] -= damage  # down
    if is_inside(row, col - 1) and alive(row, col - 1):
        m[row][col - 1] -= damage  # left
    if is_inside(row, col + 1) and alive(row, col + 1):
        m[row][col + 1] -= damage  # right
    if is_inside(row + 1, col + 1) and alive(row + 1, col + 1):
        m[row + 1][col + 1] -= damage  # down right diagonal
    if is_inside(row + 1, col - 1) and alive(row + 1, col - 1):
        m[row + 1][col - 1] -= damage  # down left diagonal
    if is_inside(row - 1, col + 1) and alive(row - 1, col + 1):
        m[row - 1][col + 1] -= damage  # up right diagonal
    if is_inside(row - 1, col - 1) and alive(row - 1, col - 1):
        m[row - 1][col - 1] -= damage  # up left diagonal
    return m


size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]
bombs = input().split()
if matrix:
    for coords in bombs:
        row, col = eval(coords)
        if matrix[row][col] > 0:
            dmg = matrix[row][col]
            matrix[row][col] = 0
            matrix = explosions(dmg, matrix)

alive_cells_sum = 0
alive_cells_count = 0
for row in matrix:
    for el in row:
        if el > 0:
            alive_cells_sum += el
            alive_cells_count += 1

print(f"Alive cells: {alive_cells_count}\n"
      f"Sum: {alive_cells_sum}")
[print(*row) for row in matrix]
