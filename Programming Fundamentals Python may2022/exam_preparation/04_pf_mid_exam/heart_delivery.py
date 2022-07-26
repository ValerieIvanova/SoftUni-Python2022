neighborhood = list(map(int, input().split('@')))
position = 0
while True:
    command = input().split()
    if command[0] == 'Love!':
        break
    length = int(command[1])
    position += length
    if position >= len(neighborhood):
        position = 0
    if neighborhood[position] <= 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        neighborhood[position] -= 2
        if neighborhood[position] <= 0:
            print(f"Place {position} has Valentine's day.")
        position = position

print(f"Cupid's last position was {position}.")
if sum(neighborhood) <= 0:
    print('Mission was successful.')
else:
    failed_houses = [house for house in neighborhood if house != 0]
    print(f'Cupid has failed {len(failed_houses)} places.')