saved_money = 0
while True:
    destination = input()
    if destination == 'End':
        break
    needed_money = float(input())
    while True:
        current_saved_money = float(input())
        saved_money += current_saved_money
        if saved_money >= needed_money:
            print(f'Going to {destination}!')
            saved_money = 0
            break