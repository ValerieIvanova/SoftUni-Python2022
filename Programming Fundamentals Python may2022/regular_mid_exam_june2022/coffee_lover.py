def include(item, stock_list):
    stock_list.append(item)
    return stock_list


def remove(first_or_last, coffees, stock_list):
    if first_or_last == 'first':
        del stock_list[:coffees]
    elif first_or_last == 'last':
        del stock_list[-coffees:]
    return stock_list


def prefer(first, second, stock_list):
    stock_list[first], stock_list[second] = stock_list[second], stock_list[first]
    return stock_list


coffees_in_stock = input().split()
commands = int(input())

for n in range(commands):
    command = input().split()
    command_name = command[0]
    if command_name == 'Include':
        coffee = command[1]
        coffees_in_stock = include(coffee, coffees_in_stock)
    elif command_name == 'Remove':
        first_last = command[1]
        number_of_coffees = int(command[2])
        if number_of_coffees > len(coffees_in_stock):
            continue
        coffees_in_stock = remove(first_last, number_of_coffees, coffees_in_stock)
    elif command_name == 'Prefer':
        first_coffee_index = int(command[1])
        second_coffee_index = int(command[2])
        if (first_coffee_index < 0 or first_coffee_index >= len(coffees_in_stock)) or \
                (second_coffee_index < 0 or second_coffee_index >= len(coffees_in_stock)):
            continue
        coffees_in_stock = prefer(first_coffee_index, second_coffee_index, coffees_in_stock)
    elif command_name == 'Reverse':
        coffees_in_stock.reverse()

print(f"Coffees:\n"
      f"{' '.join(coffees_in_stock)}")