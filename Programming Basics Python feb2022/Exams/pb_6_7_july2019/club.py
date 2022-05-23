goal_profit = float(input())
profit = 0

while True:
    name_of_cocktail = input()
    if name_of_cocktail == 'Party!':
        diff = abs(goal_profit - profit)
        print(f'We need {diff:.2f} leva more.')
        break
    number_of_cocktails = int(input())
    price_of_cocktails = len(name_of_cocktail) * number_of_cocktails
    if price_of_cocktails % 2 != 0:
        price_of_cocktails -= price_of_cocktails * 0.25
    profit += price_of_cocktails
    if profit >= goal_profit:
        print('Target acquired.')
        break

print(f'Club income - {profit:.2f} leva.')