number_of_chrysanthemum = int(input())
number_of_roses = int(input())
number_of_tulips = int(input())
season = input()
holiday = input()

price_of_chrysanthemum = 0
price_of_roses = 0
price_of_tulips = 0
discount = 0

if season == 'Spring' or season == 'Summer':
    price_of_chrysanthemum = 2.00
    price_of_roses = 4.10
    price_of_tulips = 2.50
elif season == 'Autumn' or season == 'Winter':
    price_of_chrysanthemum = 3.75
    price_of_roses = 4.50
    price_of_tulips = 4.15

if holiday == 'Y':
    price_of_chrysanthemum += price_of_chrysanthemum * 0.15
    price_of_roses += price_of_roses * 0.15
    price_of_tulips += price_of_tulips * 0.15

total_price = (number_of_chrysanthemum * price_of_chrysanthemum) + (number_of_roses * price_of_roses) + \
              (number_of_tulips * price_of_tulips)

if number_of_tulips > 7 and season == 'Spring':
    total_price -= total_price * 0.05
if number_of_roses >= 10 and season == 'Winter':
    total_price -= total_price * 0.10
if (number_of_roses + number_of_tulips + number_of_chrysanthemum) >= 20:
    total_price -= total_price * 0.20

end_price = total_price + 2

print(f'{end_price:.2f}')