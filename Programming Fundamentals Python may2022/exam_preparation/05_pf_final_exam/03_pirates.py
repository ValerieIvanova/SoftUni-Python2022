def add_targets(targets):
    if city not in targets:
        targets[city] = {'population': 0, 'gold': 0}
    targets[city]['population'] += population
    targets[city]['gold'] += gold
    return targets


def plunder(targets):
    town = command[1]
    people = int(command[2])
    gold = int(command[3])
    targets[town]['population'] -= people
    targets[town]['gold'] -= gold
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    if targets[town]['population'] <= 0 or targets[town]['gold'] <= 0:
        del targets[town]
        print(f"{town} has been wiped off the map!")
    return targets


def prosper(targets):
    town = command[1]
    gold = int(command[2])
    if gold < 0:
        print("Gold added cannot be a negative number!")
        return targets
    targets[town]['gold'] += gold
    print(f"{gold} gold added to the city treasury. {town} now has {targets[town]['gold']} gold.")
    return targets


targets_info = {}
while True:
    command = input()
    if command == 'Sail':
        break
    command = command.split('||')
    city = command[0]
    population = int(command[1])
    gold = int(command[2])
    targets_info = add_targets(targets_info)

while True:
    command = input().split('=>')
    command_name = command[0]
    if command_name == 'End':
        break

    elif command_name == 'Plunder':
        targets_info = plunder(targets_info)

    elif command_name == 'Prosper':
        targets_info = prosper(targets_info)

if targets_info:
    print(f"Ahoy, Captain! There are {len(targets_info)} wealthy settlements to go to:")
    for town, info in targets_info.items():
        print(f"{town} -> Population: {info['population']} citizens, Gold: {info['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")