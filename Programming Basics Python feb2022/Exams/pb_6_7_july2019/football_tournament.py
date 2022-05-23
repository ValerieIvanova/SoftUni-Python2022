team_name = input()
number_of_games = int(input())
number_of_w = 0
number_of_d = 0
number_of_l = 0
played = True
if number_of_games == 0:
    played = False
    print(f"{team_name} hasn't played any games during this season.")

for i in range(1, number_of_games + 1):
    result = input()
    if result == 'W':
        number_of_w += 1
    elif result == 'D':
        number_of_d += 1
    elif result == 'L':
        number_of_l += 1

if played:
    total_points = (number_of_w * 3) + (number_of_d * 1)
    win_rate = number_of_w / number_of_games * 100

    print(f'{team_name} has won {total_points} points during this season.')
    print('Total stats:')
    print(f'## W: {number_of_w}')
    print(f'## D: {number_of_d}')
    print(f'## L: {number_of_l}')
    print(f'Win rate: {win_rate:.2f}%')
