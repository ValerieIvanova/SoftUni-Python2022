joinery_count = int(input())
joinery_type = input()
delivery = input()
price = 0
discount = 0
valid = True
if joinery_count < 10:
    valid = False
    print('Invalid order')
if joinery_type == '90X130':
    price = 110 * joinery_count
    if 30 < joinery_count <= 60:
        price -= price * 0.05
    elif joinery_count > 60:
        price -= price * 0.08
elif joinery_type == '100X150':
    price = 140 * joinery_count
    if 40 < joinery_count <= 80:
        price -= price * 0.06
    elif joinery_count > 80:
        price -= price * 0.10
elif joinery_type == '130X180':
    price = 190 * joinery_count
    if 20 < joinery_count <= 50:
        price -= price * 0.07
    elif joinery_count > 50:
        price -= price * 0.12
elif joinery_type == '200X300':
    price = 250 * joinery_count
    if 25 < joinery_count <= 50:
        price -= price * 0.09
    elif joinery_count > 50:
        price -= price * 0.14

if delivery == 'With delivery':
    price += 60
if joinery_count > 99:
    price -= price * 0.04
if valid:
    print(f'{price:.2f} BGN')
