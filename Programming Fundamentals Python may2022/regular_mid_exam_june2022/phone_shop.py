phones_in_stock = input().split(', ')

while True:
    command = input().split(' - ')
    command_name = command[0]
    if command_name == 'End':
        print(*phones_in_stock, sep=', ')
        break

    elif command_name == 'Add':
        phone = command[1]
        if phone not in phones_in_stock:
            phones_in_stock.append(phone)
        else:
            continue

    elif command_name == 'Remove':
        phone = command[1]
        if phone in phones_in_stock:
            phones_in_stock.remove(phone)
        else:
            continue

    elif command_name == 'Bonus phone':
        old_new = command[1].split(':')
        old_phone = old_new[0]
        new_phone = old_new[1]
        if old_phone in phones_in_stock:
            old_phone_index = phones_in_stock.index(old_phone)
            phones_in_stock.insert(old_phone_index+1, new_phone)
        else:
            continue

    elif command_name == 'Last':
        phone = command[1]
        if phone in phones_in_stock:
            phone_index = phones_in_stock.index(phone)
            phones_in_stock.append(phones_in_stock.pop(phone_index))
        else:
            continue