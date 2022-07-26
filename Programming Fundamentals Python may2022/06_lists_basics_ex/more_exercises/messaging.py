numbers_str = input().split()
string = input()
message = ''
new_string = string
for element in numbers_str:
    current_index = 0
    for digit in range(len(element)):
        current_index += int(element[digit])
    if current_index > len(new_string):
        current_index -= len(new_string)
        message += new_string[current_index]
        new_string = new_string[:current_index] + new_string[current_index + 1:]
    else:
        message += new_string[current_index]
        new_string = new_string[:current_index] + new_string[current_index + 1:]
print(message)