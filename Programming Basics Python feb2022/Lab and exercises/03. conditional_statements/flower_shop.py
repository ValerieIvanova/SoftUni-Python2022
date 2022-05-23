from math import floor, ceil
magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cactus = int(input())
gift_price = float(input())

profit = (magnolias * 3.25) + (hyacinths * 4) + (roses * 3.50) + (cactus * 8)
tax = profit * 0.05
income = profit - tax
diff = abs(income - gift_price)

if income >= gift_price:
    print(f"She is left with {floor(diff)} leva.")
else:
    print(f"She will have to borrow {ceil(diff)} leva.")
