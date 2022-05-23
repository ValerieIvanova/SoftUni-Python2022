season = input()
type_of_group = input()
number_of_students = int(input())
days = int(input())

price = 0
sports = ''

if season == 'Winter':
    if type_of_group == 'girls':
        price = 9.60
        sports = 'Gymnastics'
    elif type_of_group == 'boys':
        price = 9.60
        sports = 'Judo'
    elif type_of_group == 'mixed':
        price = 10
        sports = 'Ski'
elif season == 'Spring':
    if type_of_group == 'girls':
        price = 7.20
        sports = 'Athletics'
    elif type_of_group == 'boys':
        price = 7.20
        sports = 'Tennis'
    elif type_of_group == 'mixed':
        price = 9.50
        sports = 'Cycling'
elif season == 'Summer':
    if type_of_group == 'girls':
        price = 15
        sports = 'Volleyball'
    elif type_of_group == 'boys':
        price = 15
        sports = 'Football'
    elif type_of_group == 'mixed':
        price = 20
        sports = 'Swimming'

total_price = number_of_students * (days * price)

if number_of_students >= 50:
    total_price -= total_price * 0.50
elif 20 <= number_of_students < 50:
    total_price -= total_price * 0.15
elif 10 <= number_of_students < 20:
    total_price -= total_price * 0.05

print(f'{sports} {total_price:.2f} lv.')