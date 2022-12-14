def check_for_item(r_, c_):
    if workshop[r_][c_] in total_items:
        total_items[workshop[r_][c_]] -= 1
        collected_items[workshop[r_][c_]] += 1
    return total_items, collected_items


def directions(my_pos_, direction_, steps_):
    global total_items, collected_items, merry_christmas
    steps_ = int(steps_)
    r, c = my_pos_[0], my_pos_[1]
    workshop[r][c] = 'x'

    for _ in range(steps_):
        if direction_ == 'right':
            if c + 1 == cols:
                c = -1
            c += 1
            total_items, collected_items = check_for_item(r, c)
            workshop[r][c] = 'x'

        elif direction_ == 'left':
            if c - 1 < 0:
                c = cols
            c -= 1
            total_items, collected_items = check_for_item(r, c)
            workshop[r][c] = 'x'

        elif direction_ == 'up':
            if r - 1 < 0:
                r = rows
            r -= 1
            total_items, collected_items = check_for_item(r, c)
            workshop[r][c] = 'x'

        elif direction_ == 'down':
            if r + 1 == rows:
                r = -1
            r += 1
            total_items, collected_items = check_for_item(r, c)
            workshop[r][c] = 'x'

        if not any(total_items.values()):
            merry_christmas = True
            workshop[r][c] = 'Y'
            return workshop, total_items, collected_items

    my_pos_[0], my_pos_[1] = r, c

    workshop[my_pos_[0]][my_pos_[1]] = 'Y'
    return workshop, total_items, collected_items


rows, cols = list(map(int, input().split(', ')))

workshop = []
my_pos = []

total_items = {
    'D': 0,
    'G': 0,
    'C': 0,
}

collected_items = {
    'D': 0,
    'G': 0,
    'C': 0,
}

for row in range(rows):
    line = input().split()
    if 'Y' in line:
        my_pos = [row, line.index('Y')]
    if 'C' in line:
        total_items['C'] += line.count('C')
    if 'G' in line:
        total_items['G'] += line.count('G')
    if 'D' in line:
        total_items['D'] += line.count('D')
    workshop.append(line)

merry_christmas = False
while True:
    command = input()
    if command == 'End':
        break
    direction, steps = command.split('-')
    workshop, total_items, collected_items = directions(my_pos, direction, steps)
    if merry_christmas:
        print("Merry Christmas!")
        break

print("You've collected:")
print(f"- {collected_items['D']} Christmas decorations\n"
      f"- {collected_items['G']} Gifts\n"
      f"- {collected_items['C']} Cookies")
[print(*row) for row in workshop]
