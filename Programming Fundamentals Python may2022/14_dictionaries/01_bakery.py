stock = input().split()
bakery = {stock[i]: int(stock[i+1]) for i in range(0, len(stock), 2)}
print(bakery)