days = int(input())
hours_per_day = int(input())
price = 0
total_price = 0
for d in range(1, days + 1):
    for h in range(1, hours_per_day + 1):
        if d % 2 == 0 and h % 2 != 0:
            price += 2.50
        elif d % 2 != 0 and h % 2 == 0:
            price += 1.25
        else:
            price += 1
    total_price += price
    print(f"Day: {d} - {price:.2f} leva")
    price = 0
print(f'Total: {total_price:.2f} leva')