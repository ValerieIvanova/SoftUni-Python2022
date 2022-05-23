city = input()
package_type = input()
vip = input()
days = int(input())
price = 0
condition = True
if city == 'Bansko' or city == 'Borovets':
    if package_type == 'noEquipment':
        price = 80
        if vip == 'yes':
            price -= price * 0.05
        elif vip == 'no':
            price = 80
    elif package_type == 'withEquipment':
        price = 100
        if vip == 'yes':
            price -= price * 0.10
        elif vip == 'no':
            price = 100
    else:
        condition = False
        print('Invalid input!')
elif city == 'Varna' or city == 'Burgas':
    if package_type == 'noBreakfast':
        price = 100
        if vip == 'yes':
            price -= price * 0.07
        elif vip == 'no':
            price = 100
    elif package_type == 'withBreakfast':
        price = 130
        if vip == 'yes':
            price -= price * 0.12
        elif vip == 'no':
            price = 130
    else:
        condition = False
        print('Invalid input!')
else:
    condition = False
    print("Invalid input!")
total_price = days * price
if days > 7:
    total_price = total_price - price
if days < 1:
    condition = False
    print("Days must be positive number!")
if condition:
    print(f"The price is {total_price:.2f}lv! Have a nice time!")