from collections import defaultdict

phonebook = defaultdict(str)
searched_contacts = 0
while True:
    command = input()
    if command.isdigit():
        searched_contacts = int(command)
        break
    name, number = command.split('-')
    phonebook[name] = number

for c in range(searched_contacts):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")