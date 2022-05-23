price_kg_veg = float(input())
price_kg_fruit = float(input())
total_kg_veg = int(input())
total_kg_fruit = int(input())

total_veg = price_kg_veg * total_kg_veg
total_fruit = price_kg_fruit * total_kg_fruit
total_income_bgn = total_fruit + total_veg

total_income_eur = total_income_bgn / 1.94

print(f'{total_income_eur:.2f}')