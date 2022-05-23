projection = input()
type = input()
tickets = int(input())
price = 0
if projection == 'John Wick':
    if type == 'Drink':
        price = 12
    elif type == 'Popcorn':
        price = 15
    elif type == 'Menu':
        price = 19
elif projection == 'Star Wars':
    if type == 'Drink':
        price = 18
    elif type == 'Popcorn':
        price = 25
    elif type == 'Menu':
        price = 30
elif projection == 'Jumanji':
    if type == 'Drink':
        price = 9
    elif type == 'Popcorn':
        price = 11
    elif type == 'Menu':
        price = 14
if projection == "Star Wars" and tickets >= 4:
    price -= price * 0.30
elif projection == 'Jumanji' and tickets == 2:
    price -= price * 0.15
total_price = price * tickets
print(f'Your bill is {total_price:.2f} leva.')