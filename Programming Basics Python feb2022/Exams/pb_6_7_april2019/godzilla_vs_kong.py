budget = float(input())
statists = int(input())
clothes_per_statist = float(input())

discount = 0
decor = budget * 0.10
clothes = statists * clothes_per_statist

if statists > 150:
    discount = clothes * 0.10

total = decor + clothes - discount
diff = abs(budget - total)

if total > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print('Action!')
    print(f"Wingard starts filming with {diff:.2f} leva left.")
