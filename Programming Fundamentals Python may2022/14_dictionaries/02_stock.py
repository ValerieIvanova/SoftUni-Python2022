stock = input().split()
products = input().split()
stock_dict = {stock[i]: int(stock[i+1]) for i in range(0, len(stock), 2)}

for p in products:
    if p in stock_dict:
        print(f"We have {stock_dict[p]} of {p} left")
    else:
        print(f"Sorry, we don't have {p}")