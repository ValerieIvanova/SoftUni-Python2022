def add_players(player_, position_, skill_):
    if player_ not in players_pool:
        players_pool[player_] = {}
    if position_ not in players_pool[player_]:
        players_pool[player_][position_] = 0
    if int(skill_) > players_pool[player_][position_]:
        players_pool[player_][position_] = int(skill_)
    return players_pool


def p_vs_p(p_1, p_2):
    if (p_1 and p_2) in players_pool:
        for first_player in players_pool[p_1]:
            if first_player in players_pool[p_2]:
                first_player_total = sum(players_pool[p_1].values())
                second_player_total = sum(players_pool[p_2].values())
                if first_player_total > second_player_total:
                    del players_pool[p_2]
                else:
                    del players_pool[p_1]
                break
    return players_pool


players_pool = {}

while True:
    command = input()
    if command == 'Season end':
        break
    if '->' in command:
        player, position, skill = command.split(' -> ')
        players_pool = add_players(player, position, skill)

    elif 'vs' in command:
        player_1, player_2 = command.split(' vs ')
        players_pool = p_vs_p(player_1, player_2)

for player, skills in sorted(players_pool.items(), key=lambda x: (-sum(x[1].values()), x[0])):
    print(f"{player}: {sum(skills.values())} skill")
    for pos, points in sorted(skills.items(), key=lambda x: (-x[1], x[0])):
        print(f"- {pos} <::> {points}")