products_info = {}
while True:
    command = input()
    if command == 'buy':
        break
    product, price, quantity = command.split()
    if product in products_info:
        products_info[product]['quantity'] += int(quantity)
        products_info[product]['price'] = float(price)
    else:
        products_info[product] = {}
        products_info[product]['quantity'] = int(quantity)
        products_info[product]['price'] = float(price)
for name, info in products_info.items():
    print(f"{name} -> {info['quantity'] * info['price']:.2f}")