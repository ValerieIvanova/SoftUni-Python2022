string = input()
new_string = ''
last_letter = ''
for char in string:
    if char != last_letter:
        last_letter = char
        new_string += char
print(new_string)