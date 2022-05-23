budget = float(input())
category = input()
number_of_people = int(input())

ticket_price = 0
transport = 0

if category == 'VIP':
    ticket_price = 499.99
elif category == 'Normal':
    ticket_price = 249.99

if 1 <= number_of_people <= 4:
    transport = budget * 0.75
elif 5 <= number_of_people <= 9:
    transport = budget * 0.60
elif 10 <= number_of_people <= 24:
    transport = budget * 0.50
elif 25 <= number_of_people <= 49:
    transport = budget * 0.40
elif number_of_people >= 50:
    transport = budget * 0.25

total_costs = transport + ticket_price * number_of_people
diff = abs(budget - total_costs)

if budget >= total_costs:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
