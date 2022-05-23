budget = int(input())
season = input()
count_of_fishers = int(input())

costs = 0

if season == 'Spring':
    costs = 3000
elif season == 'Summer' or season == 'Autumn':
    costs = 4200
elif season == 'Winter':
    costs = 2600

if count_of_fishers <= 6:
    costs -= costs * 0.1
elif 7 <= count_of_fishers <= 11:
    costs -= costs * 0.15
elif count_of_fishers >= 12:
    costs -= costs * 0.25

if count_of_fishers % 2 == 0 and season != 'Autumn':
    costs -= costs * 0.05

diff = abs(budget - costs)

if budget >= costs:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
