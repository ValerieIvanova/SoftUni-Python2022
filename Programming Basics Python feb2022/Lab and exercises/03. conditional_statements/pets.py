from math import floor, ceil
days = int(input())
food_kg = int(input())
dog_food_per_day_kg = float(input())
cat_food_per_day_kg = float(input())
turtle_food_per_day_g = float(input())

dog_food_needed = days * dog_food_per_day_kg
cat_food_needed = days * cat_food_per_day_kg
turtle_food_needed = (days * turtle_food_per_day_g) / 1000
total_food_kg = dog_food_needed + cat_food_needed + turtle_food_needed
diff = abs(total_food_kg - food_kg)

if food_kg >= total_food_kg:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")
