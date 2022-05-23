budget = float(input())
destination = input()
season = input()
days = int(input())
price = 0

if destination == 'Dubai':
    if season == 'Winter':
        price = 45000
    elif season == 'Summer':
        price = 40000
elif destination == 'Sofia':
    if season == 'Winter':
        price = 17000
    elif season == 'Summer':
        price = 12500
elif destination == 'London':
    if season == 'Winter':
        price = 24000
    elif season == 'Summer':
        price = 20250
total_price = days * price
if destination == 'Dubai':
    total_price -= total_price * 0.30
elif destination == 'Sofia':
    total_price += total_price * 0.25
diff = abs(budget - total_price)
if total_price <= budget:
    print(f'The budget for the movie is enough! We have {diff:.2f} leva left!')
else:
    print(f'The director needs {diff:.2f} leva more!')