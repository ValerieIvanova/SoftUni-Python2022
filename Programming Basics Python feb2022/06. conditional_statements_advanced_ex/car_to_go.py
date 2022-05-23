budget = float(input())
season = input()

class_of_car = ''
type_of_car = ''
price = 0

if budget <= 100:
    class_of_car = 'Economy class'
    if season == 'Summer':
        type_of_car = 'Cabrio'
        price = 0.35
    elif season == 'Winter':
        type_of_car = 'Jeep'
        price = 0.65
elif 100 < budget <= 500:
    class_of_car = 'Compact class'
    if season == 'Summer':
        type_of_car = 'Cabrio'
        price = 0.45
    elif season == 'Winter':
        type_of_car = 'Jeep'
        price = 0.80
elif budget > 500:
    class_of_car = 'Luxury class'
    type_of_car = 'Jeep'
    price = 0.90

total_price = budget * price

print(f'{class_of_car}')
print(f'{type_of_car} - {total_price:.2f}')
