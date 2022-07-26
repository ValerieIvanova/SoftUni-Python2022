list_of_numbers_str = input().split()
new_list = list_of_numbers_str
while True:
    command = input()
    if command == 'end':
        break
    command_info = command.split()
    command_name = command_info[0]

    if command_name == 'exchange':
        index = int(command_info[1])
        if index < 0 or index >= len(new_list):
            print('Invalid index')
            continue
        first_list = new_list[index + 1:]
        second_list = new_list[:index + 1]
        new_list = first_list + second_list

    elif command_name == 'max':
        even_odd = command_info[1]
        max_odd = -1
        max_even = -1
        max_even_index = 0
        max_odd_index = 0
        no_matches = False
        for i in range(len(new_list)):
            if int(new_list[i]) % 2 == 0:
                if int(new_list[i]) >= max_even:
                    max_even = int(new_list[i])
                    max_even_index = i
            elif int(new_list[i]) % 2 != 0:
                if int(new_list[i]) >= max_odd:
                    max_odd = int(new_list[i])
                    max_odd_index = i
        if even_odd == 'even' and max_even == -1:
            no_matches = True
        elif even_odd == 'odd' and max_odd == -1:
            no_matches = True
        if not no_matches and even_odd == 'even':
            print(max_even_index)
        elif not no_matches and even_odd == 'odd':
            print(max_odd_index)
        else:
            print('No matches')

    elif command_name == 'min':
        even_odd = command_info[1]
        min_odd = 1001
        min_even = 1001
        min_even_index = len(new_list)
        min_odd_index = len(new_list)
        no_matches = False
        for i in range(len(new_list)):
            if int(new_list[i]) % 2 == 0:
                if int(new_list[i]) <= min_even:
                    min_even = int(new_list[i])
                    min_even_index = i
            elif int(new_list[i]) % 2 != 0:
                if int(new_list[i]) <= min_odd:
                    min_odd = int(new_list[i])
                    min_odd_index = i
        if even_odd == 'even' and min_even == 1001:
            no_matches = True
        elif even_odd == 'odd' and min_odd == 1001:
            no_matches = True
        if not no_matches and even_odd == 'even':
            print(min_even_index)
        elif not no_matches and even_odd == 'odd':
            print(min_odd_index)
        else:
            print('No matches')

    elif command_name == 'first':
        count = int(command_info[1])
        if count > len(new_list):
            print('Invalid count')
            continue
        even_odd = command_info[2]
        first_even = []
        first_odd = []
        for element in new_list:
            if int(element) % 2 == 0:
                first_even.append(int(element))
            elif int(element) % 2 != 0:
                first_odd.append(int(element))
        if even_odd == 'even':
            first_even = first_even[:count]
            print(first_even)
        elif even_odd == 'odd':
            first_odd = first_odd[:count]
            print(first_odd)

    elif command_name == 'last':
        count = int(command_info[1])
        if count > len(new_list):
            print('Invalid count')
            continue
        even_odd = command_info[2]
        last_even = []
        last_odd = []
        for element in new_list:
            if int(element) % 2 == 0:
                last_even.append(int(element))
            elif int(element) % 2 != 0:
                last_odd.append(int(element))
        if even_odd == 'even':
            if count >= len(last_even):
                print(last_even)
            else:
                print(last_even[-count:])
        elif even_odd == 'odd':
            if count >= len(last_odd):
                print(last_odd)
            else:
                last_odd = last_odd[-count:]
                print(last_odd)
print(list(map(int, new_list)))