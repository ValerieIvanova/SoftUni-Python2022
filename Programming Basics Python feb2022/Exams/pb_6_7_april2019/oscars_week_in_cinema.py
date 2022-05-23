movie_name = input()
type_of_hall = input()
number_of_tickets = int(input())
price = 0
if movie_name == 'A Star Is Born':
    if type_of_hall == 'normal':
        price = 7.50
    elif type_of_hall == 'luxury':
        price = 10.50
    elif type_of_hall == 'ultra luxury':
        price = 13.50
elif movie_name == 'Bohemian Rhapsody':
    if type_of_hall == 'normal':
        price = 7.35
    elif type_of_hall == 'luxury':
        price = 9.45
    elif type_of_hall == 'ultra luxury':
        price = 12.75
elif movie_name == 'Green Book':
    if type_of_hall == 'normal':
        price = 8.15
    elif type_of_hall == 'luxury':
        price = 10.25
    elif type_of_hall == 'ultra luxury':
        price = 13.25
elif movie_name == 'The Favourite':
    if type_of_hall == 'normal':
        price = 8.75
    elif type_of_hall == 'luxury':
        price = 11.55
    elif type_of_hall == 'ultra luxury':
        price = 13.95

profit = number_of_tickets * price

print(f'{movie_name} -> {profit:.2f} lv.')