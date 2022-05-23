budget = float(input())
number_of_extras = int(input())
price_for_clothes_per_one_person = float(input())

price_for_decor = budget * 0.1
price_for_clothes = number_of_extras * price_for_clothes_per_one_person

if number_of_extras > 150:
    price_for_clothes -= price_for_clothes * 0.10

total_cost = price_for_decor + price_for_clothes

diff = abs(budget - total_cost)
if total_cost > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")