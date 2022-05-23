budget = float(input())
fuel_liters = float(input())
day = input()

fuel_price = fuel_liters * 2.10
total_price = fuel_price + 100
discount = 0

if day == 'Saturday':
    discount = 0.10
elif day == 'Sunday':
    discount = 0.20

final_price = total_price - (total_price * discount)
diff = abs(budget - final_price)
if budget >= final_price:
    print(f'Safari time! Money left: {diff:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {diff:.2f} lv.')