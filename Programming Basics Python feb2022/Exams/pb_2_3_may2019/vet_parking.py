days = int(input())
hours = int(input())
tax = 0
total = 0
for d in range(1, (days + 1)):
    for h in range(1, (hours + 1)):
        if d % 2 == 0 and h % 2 != 0:
            tax += 2.50
        elif d % 2 != 0 and h % 2 == 0:
            tax += 1.25
        else:
            tax += 1
    print(f'Day: {d} - {tax:.2f} leva')
    total += tax
    tax = 0
print(f'Total: {total:.2f} leva')