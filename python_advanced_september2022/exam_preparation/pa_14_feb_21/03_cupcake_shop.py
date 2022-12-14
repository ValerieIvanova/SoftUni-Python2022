def stock_availability(flavours: list, action: str, *args):
    if action == 'delivery':
        flavours.extend(args)
    elif action == 'sell':
        if not args:
            flavours.pop(0)
        elif isinstance(args[0], int):
            flavours = flavours[args[0]::]
        else:
            for order in args:
                if order in flavours:
                    product_count = flavours.count(order)
                    for i in range(product_count):
                        flavours.remove(order)

    return flavours


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 2))
