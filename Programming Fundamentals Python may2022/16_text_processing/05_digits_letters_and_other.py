string = input()
[print(digit, end='') for digit in string if digit.isdigit()]
print()
[print(letter, end='') for letter in string if letter.isalpha()]
print()
[print(char, end='') for char in string if not char.isalnum()]