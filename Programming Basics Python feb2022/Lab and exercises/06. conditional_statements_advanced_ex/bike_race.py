number_junior_bikers = int(input())
number_senior_bikers = int(input())
type_of_route = input()

junior_tax = 0
senior_tax = 0
total_tax = 0

if type_of_route == 'trail':
    junior_tax = 5.50
    senior_tax = 7
elif type_of_route == 'cross-country':
    junior_tax = 8
    senior_tax = 9.50
elif type_of_route == 'downhill':
    junior_tax = 12.25
    senior_tax = 13.75
elif type_of_route == 'road':
    junior_tax = 20
    senior_tax = 21.50

total_tax = (junior_tax * number_junior_bikers) + (senior_tax * number_senior_bikers)
if number_senior_bikers + number_junior_bikers >= 50 and type_of_route == 'cross-country':
    total_tax -= total_tax * 0.25

donation = total_tax - (total_tax * 0.05)

print(f'{donation:.2f}')
