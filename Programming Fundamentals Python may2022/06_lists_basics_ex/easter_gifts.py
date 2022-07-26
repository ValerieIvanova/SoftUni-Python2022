planned_gifts = input().split()
while True:
    command = input()
    if command == 'No Money':
        break
    command_info = command.split()
    command_name = command_info[0]
    command_gift = command_info[1]
    if command_name == 'OutOfStock':
        if command_gift in planned_gifts:
            for gift in range(len(planned_gifts)):
                if planned_gifts[gift] == command_gift:
                    planned_gifts[gift] = 'None'
    elif command_name == 'Required':
        command_index = int(command_info[2])
        if 0 <= command_index < len(planned_gifts):
            planned_gifts[command_index] = command_gift
    elif command_name == 'JustInCase':
        planned_gifts[-1] = command_gift
new_gift_list = [gifts for gifts in planned_gifts if gifts != 'None']
print(' '.join(new_gift_list))