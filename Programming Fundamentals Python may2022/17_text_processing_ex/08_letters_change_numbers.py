def string_operations(front_let, back_let, num):
    total = 0
    if front_let.isupper():
        front_let = front_let.lower()
        total += int(num) / (ord(front_let) - 96)
    elif front_let.islower():
        total += int(num) * (ord(front_let) - 96)
    if back_let.isupper():
        back_let = back_let.lower()
        total -= (ord(back_let) - 96)
    elif back_let.islower():
        total += (ord(back_let) - 96)
    return total


strings = input().split()
total_sum = 0

for string in strings:
    number = ''
    letter_in_front = ''
    letter_in_back = ''
    for i in range(len(string)):
        if string[i].isalpha() and len(letter_in_front) > 0:
            letter_in_back = string[i]
        elif string[i].isalpha() and len(letter_in_front) == 0:
            letter_in_front = string[i]
        elif string[i].isdigit():
            number += string[i]

    total_sum += string_operations(letter_in_front, letter_in_back, number)
print(f'{total_sum:.2f}')
