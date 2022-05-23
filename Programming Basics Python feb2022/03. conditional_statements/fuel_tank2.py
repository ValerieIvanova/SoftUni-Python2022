fuel_type = input()
fuel_liters = float(input())
discount_card_y_n = input()
card_discount = 0
liters_discount = 0
fuel_price = 0

if fuel_type == 'Gas':
    fuel_price = 0.93
    if discount_card_y_n == 'Yes':
        card_discount = 0.08
    elif discount_card_y_n == 'No':
        card_discount = 0
elif fuel_type == 'Diesel':
    fuel_price = 2.33
    if discount_card_y_n == 'Yes':
        card_discount = 0.12
    elif discount_card_y_n == 'No':
        card_discount = 0
elif fuel_type == 'Gasoline':
    fuel_price = 2.22
    if discount_card_y_n == 'Yes':
        card_discount = 0.18
    elif discount_card_y_n == 'No':
        card_discount = 0

if 20 < fuel_liters <= 25:
    liters_discount = 0.08
elif fuel_liters > 25:
    liters_discount = 0.1

fuel_price_with_discount = fuel_price - card_discount
total_fuel_price = fuel_liters * fuel_price_with_discount
end_price = total_fuel_price - (total_fuel_price * liters_discount)
print(f'{end_price:.2f} lv.')