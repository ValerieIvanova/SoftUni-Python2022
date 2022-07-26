while True:
    string = input()
    if string == 'End':
        break
    if string == 'SoftUni':
        continue
    for char in string:
        print(2 * char, end='')
    print()