budget = float(input())
price_per_kg_flour = float(input())
price_for_eggs = 0.75 * price_per_kg_flour
price_for_milk = price_per_kg_flour * 1.25
price_for_250ml_milk = (price_for_milk / 1) * 0.250
counter = 0
colored_eggs = 0
while True:
    loaf = price_for_eggs + price_per_kg_flour + price_for_250ml_milk
    if loaf > budget:
        break
    budget -= loaf
    counter += 1
    colored_eggs += 3
    if counter % 3 == 0:
        colored_eggs -= counter - 2

print(f'You made {counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
