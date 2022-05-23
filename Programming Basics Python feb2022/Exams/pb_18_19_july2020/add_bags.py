price_of_luggage_20kg = float(input())
luggage_kg = float(input())
days_to_flight = int(input())
luggage_count = int(input())
price_of_luggage = 0

if luggage_kg < 10:
    price_of_luggage = price_of_luggage_20kg * 0.2
elif 10 <= luggage_kg <= 20:
    price_of_luggage = price_of_luggage_20kg * 0.5
else:
    price_of_luggage = price_of_luggage_20kg

days_to_flight_tax = 0
if days_to_flight > 30:
    days_to_flight_tax = 0.1
elif 7 <= days_to_flight <= 30:
    days_to_flight_tax = 0.15
elif days_to_flight < 7:
    days_to_flight_tax = 0.4

price_of_luggage_nkg = price_of_luggage
increase_of_the_lug_price = price_of_luggage_nkg + (price_of_luggage_nkg * days_to_flight_tax)

total_price = (f"{increase_of_the_lug_price * luggage_count:.2f}")
print(f"The total price of bags is: {total_price} lv.")
