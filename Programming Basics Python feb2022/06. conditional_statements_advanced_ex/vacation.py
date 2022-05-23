budget = float(input())
season = input()

property = ''
location = ''
price = 0

if budget <= 1000:
    property = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        price = 0.65
    elif season == 'Winter':
        location = 'Morocco'
        price = 0.45
elif 1000 < budget <= 3000:
    property = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        price = 0.80
    elif season == 'Winter':
        location = 'Morocco'
        price = 0.60
elif budget > 3000:
    property = 'Hotel'
    price = 0.90
    if season == 'Summer':
        location = 'Alaska'
    elif season == 'Winter':
        location = 'Morocco'

total_price = budget * price

print(f"{location} - {property} - {total_price:.2f}")
