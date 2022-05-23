voucher = int(input())
ticket = 0
others = 0
price = 0
while True:
    bought_item = input()
    if bought_item == 'End':
        break
    if len(bought_item) > 8:
        price = ord(bought_item[0]) + ord(bought_item[1])
        if price <= voucher:
            ticket += 1
        else:
            break
    elif len(bought_item) <= 8:
        price = ord(bought_item[0])
        if price <= voucher:
            others += 1
        else:
            break
    voucher -= price
print(f'{ticket}')
print(f'{others}')