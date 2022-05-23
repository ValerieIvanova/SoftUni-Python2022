budget = float(input())
season = input()

costs = 0
destination = ''
property = ''

if budget <=100:
    destination = 'Bulgaria'
    if season == 'summer':
        property = 'Camp'
        costs = budget * 0.30
    elif season == 'winter':
        property = 'Hotel'
        costs = budget * 0.70
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        property = 'Camp'
        costs = budget * 0.40
    elif season == 'winter':
        property = 'Hotel'
        costs = budget * 0.80
else:
    destination = 'Europe'
    property = 'Hotel'
    costs = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{property} - {costs:.2f}")
