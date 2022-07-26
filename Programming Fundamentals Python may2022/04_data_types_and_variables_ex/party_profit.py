group_size = int(input())
days = int(input())
coins_for_companions = 0
coins_earned = 0
for day in range(1, days + 1):
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    coins_for_companions += 2 * group_size
    coins_earned += 50
    if day % 3 == 0:
        coins_for_companions += 3 * group_size
    if day % 5 == 0:
        coins_earned += 20 * group_size
        if day % 3 == 0:
            coins_for_companions += 2 * group_size
total_coins = coins_earned - coins_for_companions
coins_per_companion = int(total_coins / group_size)
print(f'{group_size} companions received {coins_per_companion} coins each.')