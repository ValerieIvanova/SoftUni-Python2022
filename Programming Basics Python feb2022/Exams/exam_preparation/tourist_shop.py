budget = float(input())
counter = 0
price = 0
while True:
    product_name = input()
    if product_name == 'Stop':
        print(f"You bought {counter} products for {price:.2f} leva.")
        break
    product_price = float(input())
    counter += 1
    if counter % 3 == 0:
        product_price = product_price / 2
    if product_price > budget:
        counter -= 1
        diff = abs(budget - product_price)
        print("You don't have enough money!")
        print(f"You need {diff:.2f} leva!")
        break
    budget -= product_price
    price += product_price