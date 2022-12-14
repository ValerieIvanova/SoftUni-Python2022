size = int(input())
wonder_territory = []
tea_bags = 0
alice_pos = []

for row in range(size):
    line = input().split()
    wonder_territory.append(line)
    if 'A' in line:
        alice_pos = [row, line.index('A')]
        wonder_territory[row][alice_pos[1]] = '*'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while tea_bags < 10:
    command = input()
    row = alice_pos[0] + directions[command][0]
    col = alice_pos[1] + directions[command][1]

    if False in [0 <= row < size, 0 <= col < size]:
        break
    alice_pos = [row, col]
    position = wonder_territory[row][col]
    wonder_territory[row][col] = '*'

    if position == 'R':
        break
    if position.isdigit():
        tea_bags += int(position)

if tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")
print(*[' '. join(row) for row in wonder_territory], sep='\n')