n = int(input())
list_of_characters = [',', '.', '_']
for _ in range(n):
    not_pure = False
    string = input()
    for char in string:
        if char in list_of_characters:
            not_pure = True
            break
        else:
            continue
    if not_pure:
        print(f'{string} is not pure!')
    else:
        print(f'{string} is pure.')