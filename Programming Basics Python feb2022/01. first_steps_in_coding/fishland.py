price_mackerel_kg = float(input())
price_sprat_kg = float(input())

bonito_kg = float(input())
scad_kg = float(input())
mussels_kg = int(input())

price_bonito_kg = price_mackerel_kg + (price_mackerel_kg * 0.60)
total_bonito_price = price_bonito_kg * bonito_kg

price_scad_kg = price_sprat_kg + (price_sprat_kg * 0.8)
total_scad_price = scad_kg * price_scad_kg

total_mussels_price = mussels_kg * 7.50

check = total_bonito_price + total_scad_price + total_mussels_price

print(f"{check:.2f}")