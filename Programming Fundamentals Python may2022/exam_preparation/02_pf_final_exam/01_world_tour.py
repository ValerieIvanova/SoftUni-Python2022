def add_stop(destination):
    index = int(command[1])
    string = command[2]
    if 0 <= index < len(destination):
        destination = destination[:index] + string + destination[index:]
    return destination


def remove_stop(destination):
    start_index = int(command[1])
    end_index = int(command[2])
    if 0 <= start_index < len(destination) and 0 <= end_index < len(destination):
        destination = destination[:start_index] + destination[end_index + 1:]
    return destination


def switch(destination):
    old_string = command[1]
    new_string = command[2]
    if old_string in destination:
        destination = destination.replace(old_string, new_string)
    return destination


stops = input()

while True:
    command = input().split(':')
    command_name = command[0]
    if command_name == 'Travel':
        break
    elif command_name == 'Add Stop':
        stops = add_stop(stops)
    elif command_name == 'Remove Stop':
        stops = remove_stop(stops)
    elif command_name == 'Switch':
        stops = switch(stops)
    print(stops)

print(f"Ready for world tour! Planned stops: {stops}")