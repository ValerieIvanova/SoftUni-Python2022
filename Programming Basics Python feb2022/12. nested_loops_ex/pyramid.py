number = int(input())
condition = False
current_value = 1
for row in range(1, number + 1):
    for col in range(1, row + 1):
        if current_value > number:
            condition = True
            break
        print(f'{str(current_value)}', end=' ')
        current_value += 1
    if condition:
        break
    print()