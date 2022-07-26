def take_odd(string_):
    new_string = ''
    for i in range(len(string_)):
        if i % 2 != 0:
            new_string += string_[i]
    return new_string


def cut(string_, ind, len_):
    string_ = string_[:ind] + string_[(ind + len_):]
    return string_


def substitute_(string_, substring_, substitute__):
    if substring_ in string_:
        string_ = string_.replace(substring_, substitute__)
        return string_
    else:
        return "Nothing to replace!"


string = input()
while True:
    command = input()
    if command == 'Done':
        break
    command = command.split()

    if command[0] == 'TakeOdd':
        string = take_odd(string)
        print(string)

    elif command[0] == 'Cut':
        index = int(command[1])
        length = int(command[2])
        string = cut(string, index, length)
        print(string)

    elif command[0] == 'Substitute':
        substring = command[1]
        substitute = command[2]
        if substitute_(string, substring, substitute) != "Nothing to replace!":
            string = substitute_(string, substring, substitute)
            print(string)
        else:
            print("Nothing to replace!")

print(f"Your password is: {string}")