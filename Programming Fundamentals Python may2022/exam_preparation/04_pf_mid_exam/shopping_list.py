def urgent(groceries_list, item):
    groceries_list.insert(0, item)
    return groceries_list


def unnecessary(groceries_list, item):
    groceries_list.remove(item)
    return groceries_list


def correct(groceries_list, item1, item2):
    item_index = groceries_list.index(item1)
    groceries_list[item_index] = item2
    return groceries_list


def rearrange(groceries_list, item):
    item_index = groceries_list.index(item)
    groceries_list.append(groceries_list.pop(item_index))
    return groceries_list


groceries = input().split('!')

while True:
    command = input()
    if command == 'Go Shopping!':
        break
    command_data = command.split()
    command_name = command_data[0]
    current_item = command_data[1]
    if command_name == 'Urgent':
        if current_item not in groceries:
            groceries = urgent(groceries, current_item)
        else:
            continue

    elif command_name == 'Unnecessary':
        if current_item in groceries:
            groceries = unnecessary(groceries, current_item)
        else:
            continue

    elif command_name == 'Correct':
        if current_item in groceries:
            new_item = command_data[2]
            groceries = correct(groceries, current_item, new_item)
        else:
            continue

    elif command_name == 'Rearrange':
        if current_item in groceries:
            groceries = rearrange(groceries, current_item)
        else:
            continue
print(*groceries, sep=', ')