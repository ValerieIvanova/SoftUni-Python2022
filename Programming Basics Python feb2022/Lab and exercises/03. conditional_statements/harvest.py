import math

x = int(input())
y = float(input())
z = int(input())
workers = int(input())

total_grapes = x * y
grapes_for_wine = total_grapes * 0.40
wine = grapes_for_wine / 2.5
diff = abs(z - wine)

if wine < z:
    print(f"It will be a tough winter! More {math.floor(diff)} liters wine needed.")
elif wine >= z:
    wine_per_worker = abs(diff / workers)
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    print (f'{math.ceil(diff)} liters left -> {math.ceil(wine_per_worker)} liters per person.')
