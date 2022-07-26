def contains(key):
    substring = command[1]
    if substring in key:
        return f"{key} contains {substring}"
    return "Substring not found!"


def flip(key):
    upper_or_lower = command[1]
    start_index = int(command[2])
    end_index = int(command[3])
    if upper_or_lower == 'Upper':
        key = key[:start_index] + (key[start_index:end_index]).upper() + \
                             key[end_index:]
    elif upper_or_lower == 'Lower':
        key = key[:start_index] + (key[start_index:end_index]).lower() + \
              key[end_index:]
    return key


def slice_(key):
    start_index = int(command[1])
    end_index = int(command[2])
    key = key[:start_index] + key[end_index:]
    return key


activation_key = input()

while True:
    command = input().split('>>>')
    command_name = command[0]
    if command_name == 'Generate':
        break

    elif command_name == 'Contains':
        print(contains(activation_key))
        continue

    elif command_name == 'Flip':
        activation_key = flip(activation_key)

    elif command_name == 'Slice':
        activation_key = slice_(activation_key)

    print(activation_key)

print(f'Your activation key is: {activation_key}')