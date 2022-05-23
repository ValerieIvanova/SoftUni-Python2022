budget = float(input())
money_spent = 0
products_bought = 0
while True:
    product_name = input()
    if product_name == 'Stop':
        print(f'You bought {products_bought} products for {money_spent:.2f} leva.')
        break
    product_price = float(input())
    products_bought += 1
    if products_bought % 3 == 0:
        product_price = product_price / 2
    if product_price > budget:
        print("You don't have enough money!")
        diff = abs(budget - product_price)
        print(f'You need {diff:.2f} leva!')
        break
    budget -= product_price
    money_spent += product_price