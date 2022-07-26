# pirate_ship = list(map(int, input().split('>')))
# warship_status = list(map(int, input().split('>')))
# max_health_capacity = int(input())
# battle_finished = False
#
# while True:
#     command = input().split()
#     command_name = command[0]
#     if command_name == 'Retire':
#         print(f"Pirate ship status: {sum(pirate_ship)}\n"
#               f"Warship status: {sum(warship_status)}")
#         break
#     elif command_name == 'Fire':
#         index = int(command[1])
#         damage = int(command[2])
#         if 0 <= index < len(warship_status):
#             if warship_status[index] - damage <= 0:
#                 print("You won! The enemy ship has sunken.")
#                 battle_finished = True
#                 break
#             else:
#                 warship_status[index] -= damage
#
#     elif command_name == 'Defend':
#         start_index = int(command[1])
#         end_index = int(command[2])
#         damage = int(command[3])
#         if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
#             for s in range(start_index, end_index+1):
#                 if pirate_ship[s] - damage <= 0:
#                     print("You lost! The pirate ship has sunken.")
#                     battle_finished = True
#                     break
#                 pirate_ship[s] -= damage
#
#     elif command_name == 'Repair':
#         index = int(command[1])
#         health = int(command[2])
#         if 0 <= index < len(pirate_ship):
#             if pirate_ship[index] + health <= max_health_capacity:
#                 pirate_ship[index] += health
#             else:
#                 diff = max_health_capacity - pirate_ship[index]
#                 pirate_ship[index] += diff
#
#     elif command_name == 'Status':
#         repair_sections = [s for s in pirate_ship if s < (max_health_capacity * 0.2)]
#         print(f'{len(repair_sections)} sections need repair.')
#
#     if battle_finished:
#         break
#
#


# With functions:
def valid_index(i, current_list):
    if 0 <= i < len(current_list):
        return True
    return False


def fire(enemy_ship):
    index = int(command[1])
    damage = int(command[2])
    if valid_index(index, enemy_ship):
        enemy_ship[index] -= damage
        if enemy_ship[index] <= 0:
            print('You won! The enemy ship has sunken.')
    return enemy_ship


def defend(our_ship):
    start_index = int(command[1])
    end_index = int(command[2])
    damage = int(command[3])
    if valid_index(start_index, our_ship) and valid_index(end_index, our_ship):
        for s in range(start_index, end_index + 1):
            our_ship[s] -= damage
            if our_ship[s] <= 0:
                break
        if any(n <= 0 for n in our_ship):
            print("You lost! The pirate ship has sunken.")
    return our_ship


def repair(our_ship):
    index = int(command[1])
    health = int(command[2])
    if valid_index(index, our_ship):
        if our_ship[index] + health <= max_health_capacity:
            our_ship[index] += health
        else:
            diff = max_health_capacity - our_ship[index]
            our_ship[index] += diff
    return our_ship


def status(our_ship):
    repair_sections = [s for s in our_ship if s < (max_health_capacity * 0.2)]
    return f"{len(repair_sections)} sections need repair."


pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
max_health_capacity = int(input())

while True:
    command = input().split()
    command_name = command[0]
    if command_name == 'Retire':
        print(f"Pirate ship status: {sum(pirate_ship)}\n"
              f"Warship status: {sum(warship)}")
        break
    elif command_name == 'Fire':
        fire(warship)
    elif command_name == 'Defend':
        defend(pirate_ship)
    elif command_name == 'Repair':
        repair(pirate_ship)
    elif command_name == 'Status':
        print(status(pirate_ship))
    if any(n <= 0 for n in pirate_ship) or any(n <= 0 for n in warship):
        break