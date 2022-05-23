points = 0
max_points = 0
winner = ''
while True:
    name = input()
    if name == 'Stop':
        break
    for char in name:
        number = int(input())
        if number == ord(char):
            points += 10
        else:
            points += 2
    if points >= max_points:
        winner = name
        max_points = points
    points = 0
print(f'The winner is {winner} with {max_points} points!')