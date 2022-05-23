best_player = ''
most_goals = 0
hat_trick = False
while True:
    player_name = input()
    if player_name == 'END':
        break
    goal_number = int(input())
    if goal_number > most_goals:
        most_goals = goal_number
        best_player = player_name
        if goal_number >= 3:
            hat_trick = True
    if goal_number >= 10:
        break
print(f"{best_player} is the best player!")
if hat_trick:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")