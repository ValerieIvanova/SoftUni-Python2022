month = input()
days = int(input())

apartment_total_cost = 0
studio_total_cost = 0

if month == 'May' or month == 'October':
    studio_total_cost = 50 * days
    if 7 < days <= 14:
        studio_total_cost -= studio_total_cost * 0.05
    elif days > 14:
        studio_total_cost -= studio_total_cost * 0.30
    apartment_total_cost = 65 * days
elif month == 'June' or month == 'September':
    studio_total_cost = 75.20 * days
    if days > 14:
        studio_total_cost -= studio_total_cost * 0.20
    apartment_total_cost = 68.70 * days
elif month == 'July' or month == 'August':
    studio_total_cost = 76 * days
    apartment_total_cost = 77 * days

if days > 14:
    apartment_total_cost -= apartment_total_cost * 0.10

print(f"Apartment: {apartment_total_cost:.2f} lv.")
print(f"Studio: {studio_total_cost:.2f} lv.")