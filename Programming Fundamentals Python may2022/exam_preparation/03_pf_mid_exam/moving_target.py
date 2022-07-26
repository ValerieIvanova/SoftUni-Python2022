def valid_index(ind, new_list):
    if 0 <= ind < len(new_list):
        return True
    else:
        return False


def shoot(ind, p):
    targets[ind] -= p
    if targets[ind] <= 0:
        targets.remove(targets[ind])
    return targets


def add(ind, v):
    targets.insert(ind, v)
    return targets


def strike(ind, r):
    del targets[ind-r:ind+r + 1]
    return targets


targets = list(map(int, input().split()))

while True:
    command_data = input().split()
    command_name = command_data[0]
    if command_name == 'End':
        print(*targets, sep='|')
        break
    index = int(command_data[1])

    if command_name == 'Shoot':
        if valid_index(index, targets):
            power = int(command_data[2])
            targets = shoot(index, power)

    elif command_name == 'Add':
        if valid_index(index, targets):
            value = int(command_data[2])
            targets = add(index, value)
        else:
            print('Invalid placement!')

    elif command_name == 'Strike':
        radius = int(command_data[2])
        if 0 + radius <= index < len(targets) - radius:
            if (0 + radius) <= radius < (len(targets)-radius):
                strike(index, radius)
            else:
                print('Strike missed!')
                continue
        else:
            print('Strike missed!')
            continue