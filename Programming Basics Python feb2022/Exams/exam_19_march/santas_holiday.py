days = int(input())
type_of_room = input()
grade = input()
nights = days - 1
price = 0
if type_of_room == 'room for one person':
    price = 18 * nights
elif type_of_room == 'apartment':
    price = 25 * nights
    if nights < 10:
        price -= price * 0.30
    elif 10 <= nights <= 15:
        price -= price * 0.35
    elif nights > 15:
        price -= price * 0.50
elif type_of_room == 'president apartment':
    price = 35 * nights
    if nights < 10:
        price -= price * 0.10
    elif 10 <= nights <= 15:
        price -= price * 0.15
    elif nights > 15:
        price -= price * 0.20

if grade == 'positive':
    price += price * 0.25
elif grade == 'negative':
    price -= price * 0.10

print(f'{price:.2f}')
