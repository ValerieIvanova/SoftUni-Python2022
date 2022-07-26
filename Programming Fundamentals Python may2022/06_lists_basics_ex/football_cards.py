list_of_cards = input().split(' ')
team_a = 11
team_b = 11
players_out = []
game_terminated = False
for card in list_of_cards:
    if card not in players_out:
        players_out.append(card)
        if card.startswith('A'):
            team_a -= 1
        elif card.startswith('B'):
            team_b -= 1
        else:
            continue
    if team_a < 7 or team_b < 7:
        game_terminated = True
        break

print(f'Team A - {team_a}; Team B - {team_b}')
if game_terminated:
    print('Game was terminated')