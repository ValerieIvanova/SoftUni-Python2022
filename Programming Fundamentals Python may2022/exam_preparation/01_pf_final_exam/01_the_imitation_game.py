def move(num, message):
    message = message[num:] + message[:num]
    return message


def insert(ind, val, message):
    message = message[:ind] + val + message[ind:]
    return message


def change_all(substr, repl, message):
    message = message.replace(substr, repl)
    return message


encrypted_message = input()
while True:
    command = input().split('|')
    command_name = command[0]
    if command_name == 'Decode':
        break
    elif command_name == 'Move':
        number_of_letters = int(command[1])
        encrypted_message = move(number_of_letters, encrypted_message)

    elif command_name == 'Insert':
        index = int(command[1])
        value = command[2]
        encrypted_message = insert(index, value, encrypted_message)

    elif command_name == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        encrypted_message = change_all(substring, replacement, encrypted_message)

print(f"The decrypted message is: {encrypted_message}")