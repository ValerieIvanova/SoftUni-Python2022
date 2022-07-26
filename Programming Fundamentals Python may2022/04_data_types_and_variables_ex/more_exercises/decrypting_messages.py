key = int(input())
number_of_lines = int(input())
message = ''
for i in range(number_of_lines):
    letter = input()
    message += chr(ord(letter) + key)
print(message)