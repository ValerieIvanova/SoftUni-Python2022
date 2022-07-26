total_price = 0
taxes = 0
total_price_with_taxes = total_price + taxes
is_special = False
is_regular = False

while True:
    parts_price = input()
    if parts_price == 'special':
        is_special = True
        total_price_with_taxes = total_price + taxes
        total_price_with_taxes -= total_price_with_taxes * 0.10
        break
    elif parts_price == 'regular':
        total_price_with_taxes = total_price + taxes
        is_regular = True
        break
    if float(parts_price) < 0:
        print('Invalid price!')
        continue
    total_price += float(parts_price)
    taxes += float(parts_price) * 0.20

if total_price == 0:
    print('Invalid order!')
else:
    if is_special or is_regular:
        print("Congratulations you've just bought a new computer!")
        print(f'Price without taxes: {total_price:.2f}$')
        print(f'Taxes: {taxes:.2f}$')
        print('-----------')
        print(f'Total price: {total_price_with_taxes:.2f}$')