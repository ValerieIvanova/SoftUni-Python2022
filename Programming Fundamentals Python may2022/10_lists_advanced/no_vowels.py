string = input()
vowels = ['a', 'o', 'u', 'e', 'i']
new_string = [char for char in string if char.lower() not in vowels]
print(''.join(new_string))