# treasure_chest = input().split('|')
#
# while True:
#     command = input().split()
#     command_name = command[0]
#     if command_name == 'Yohoho!':
#         if len(treasure_chest) > 0:
#             sum = 0
#             for item in treasure_chest:
#                 sum += len(item)
#             avr_gain = sum / len(treasure_chest)
#             print(f"Average treasure gain: {avr_gain:.2f} pirate credits.")
#         else:
#             print("Failed treasure hunt.")
#         break
#     elif command_name == 'Loot':
#         items = command[1:]
#         for item in items:
#             if item not in treasure_chest:
#                 treasure_chest.insert(0, item)
#
#     elif command_name == 'Drop':
#         index = int(command[1])
#         if 0 <= index < len(treasure_chest):
#             treasure_chest.append(treasure_chest.pop(index))
#         else:
#             continue
#
#     elif command_name == 'Steal':
#         count = int(command[1])
#         stolen = list(treasure_chest[-count:])
#         print(*stolen, sep=', ')
#         treasure_chest = treasure_chest[:-count]


# With functions:

def loot(chest):
    items = command[1:]
    for item in items:
        if item not in chest:
            chest.insert(0, item)
    return chest


def drop(chest):
    index = int(command[1])
    if 0 <= index < len(chest):
        chest.append(chest.pop(index))
    return chest


def steal(chest):
    count = int(command[1])
    stolen_items = chest[-count:]
    chest = chest[:-count]
    print(*stolen_items, sep=', ')
    return chest


def yohoho(chest):
    if len(chest) > 0:
        sum = 0
        for item in chest:
            sum += len(item)
        avr_sum = sum / len(chest)
        return f'Average treasure gain: {avr_sum:.2f} pirate credits.'
    else:
        return "Failed treasure hunt."


treasure_chest = input().split('|')

while True:
    command = input().split()
    command_name = command[0]
    if command_name == 'Yohoho!':
        print(yohoho(treasure_chest))
        break
    elif command_name == 'Loot':
        treasure_chest = loot(treasure_chest)
    elif command_name == 'Drop':
        treasure_chest = drop(treasure_chest)
    elif command_name == 'Steal':
        treasure_chest = steal(treasure_chest)