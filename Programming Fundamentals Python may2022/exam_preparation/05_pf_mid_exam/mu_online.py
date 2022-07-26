rooms = input().split('|')
health = 100
bitcoins = 0
best_room = 0
for room in rooms:
    command_data = room.split()
    command = command_data[0]
    number = int(command_data[1])
    best_room += 1
    if command == 'potion':
        if health + number <= 100:
            health += number
            print(f'You healed for {number} hp.')
        else:
            diff = 100 - health
            health += diff
            print(f'You healed for {diff} hp.')
        print(f"Current health: {health} hp.")
    elif command == 'chest':
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health <= 0:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {best_room}")
            break
        else:
            print(f"You slayed {command}.")
    if best_room == len(rooms):
        print(f"You've made it!\n"
              f"Bitcoins: {bitcoins}\n"
              f"Health: {health}")