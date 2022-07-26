decorations = int(input())
days_until_christmas = int(input())
total_cost = 0
spirit = 0

for day in range(1, days_until_christmas + 1):
    if day % 11 == 0:
        decorations += 2
    if day % 2 == 0:
        total_cost += decorations * 2
        spirit += 5
    if day % 3 == 0:
        total_cost += decorations * (5 + 3)
        spirit += 13
    if day % 5 == 0:
        total_cost += decorations * 15
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        total_cost += 5 + 3 + 15
        if days_until_christmas == day:
            spirit -= 30
print(f'Total cost: {total_cost}')
print(f'Total spirit: {spirit}')