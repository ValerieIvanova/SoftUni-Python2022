wagons = int(input())
train_list = [0 for i in range(wagons)]   # train_list = [0] * wagons

while True:
    command = input()
    if command == 'End':
        break
    command_info = command.split()
    command_name = command_info[0]
    if command_name == 'add':
        people = int(command_info[1])
        train_list[-1] += people
    elif command_name == 'insert':
        index = int(command_info[1])
        people = int(command_info[2])
        train_list[index] += people
    elif command_name == 'leave':
        index = int(command_info[1])
        people = int(command_info[2])
        train_list[index] -= people

print(train_list)