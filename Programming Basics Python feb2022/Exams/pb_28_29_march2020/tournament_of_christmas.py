days = int(input())
charity = 0
total_wins = 0
total_loses = 0
for i in range(1, days + 1):
    daily_wins = 0
    daily_loses = 0
    daily_money = 0
    while True:
        sport = input()
        if sport == 'Finish':
            break
        result = input()
        if result == 'win':
            daily_wins += 1
            daily_money += 20
        elif result == 'lose':
            daily_loses += 1
    if daily_wins > daily_loses:
        daily_money += daily_money * 0.10
        charity += daily_money
        total_wins += 1
    else:
        total_loses += 1
        charity += daily_money

if total_wins > total_loses:
    charity += charity * 0.20
    print(f"You won the tournament! Total raised money: {charity:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {charity:.2f}")
