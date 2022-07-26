lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_expenses = 0
broken_shield_count = 0

for game in range(1, lost_fights_count + 1):
    if game % 2 == 0:
        total_expenses += helmet_price
    if game % 3 == 0:
        total_expenses += sword_price
        if game % 2 == 0:
            total_expenses += shield_price
            broken_shield_count += 1
            if broken_shield_count % 2 == 0:
                total_expenses += armor_price
print(f'Gladiator expenses: {total_expenses:.2f} aureus')
