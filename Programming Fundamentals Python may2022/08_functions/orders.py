def order_price(product: str, quantity: int):
    price = 0
    if product == 'coffee':
        price = 1.50
    elif product == 'water':
        price = 1
    elif product == 'coke':
        price = 1.40
    elif product == 'snacks':
        price = 2
    return f'{price * quantity:.2f}'


current_product = input()
quantity_of_the_product = int(input())

print(order_price(current_product, quantity_of_the_product))