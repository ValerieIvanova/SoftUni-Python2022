contract_period = input()
contract_type = input()
cellular_data = input()
months = int(input())
tax = 0

if contract_period == 'one':
    if contract_type == 'Small':
        tax = 9.98
    elif contract_type == 'Middle':
        tax = 18.99
    elif contract_type == 'Large':
        tax = 25.98
    elif contract_type == 'ExtraLarge':
        tax = 35.99
elif contract_period == 'two':
    if contract_type == 'Small':
        tax = 8.58
    elif contract_type == 'Middle':
        tax = 17.09
    elif contract_type == 'Large':
        tax = 23.59
    elif contract_type == 'ExtraLarge':
        tax = 31.79

if cellular_data == 'yes':
    if tax <= 10:
        tax += 5.50
    elif 10 < tax <= 30:
        tax += 4.35
    elif tax > 30:
        tax += 3.85

if contract_period == 'two':
    tax -= tax * 0.0375

final_tax = months * tax

print(f'{final_tax:.2f} lv.')