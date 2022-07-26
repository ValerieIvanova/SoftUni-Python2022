events = input().split('|')
energy = 100
coins = 100
closed = False
for event in events:
    event_info = event.split('-')
    event_type = event_info[0]
    number = int(event_info[1])
    if event_type == 'rest':
        temp_energy = energy
        energy += number
        if energy > 100:
            energy = 100
        gained_energy = energy - temp_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')
    elif event_type == 'order':
        if energy >= 30:
            coins += number
            print(f'You earned {number} coins.')
            energy -= 30
        else:
            energy += 50
            print('You had to rest!')
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {event_type}.")
        else:
            print(f"Closed! Cannot afford {event_type}.")
            closed = True
            break
if not closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")