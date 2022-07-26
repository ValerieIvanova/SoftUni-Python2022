ticket_price = 150
items = input().split('|')
budget = int(input())
items_bought = []
profit = 0
sum_of_the_sold_items = 0
for element in items:
    item_info = element.split('->')
    type = item_info[0]
    price = float(item_info[1])
    valid = False
    selling_price = 0
    if type == 'Clothes' and 0 < price <= 50:
        valid = True
    elif type == 'Shoes' and 0 < price <= 35:
        valid = True
    elif type == 'Accessories' and 0 < price <= 20.50:
        valid = True
    if valid:
        if price <= budget:
            budget -= price
            selling_price = price + (price * 0.40)
            sum_of_the_sold_items += selling_price
            items_bought.append(f'{selling_price:.2f}')
            profit += selling_price - price

print(' '.join(items_bought))
print(f'Profit: {profit:.2f}')
if sum_of_the_sold_items + budget >= ticket_price:
    print('Hello, France!')
else:
    print('Not enough money.')