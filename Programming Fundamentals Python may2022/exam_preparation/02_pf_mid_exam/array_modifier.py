def swap(ind1, ind2):
    array_values[ind1], array_values[ind2] = array_values[ind2], array_values[ind1]
    return array_values


def multiply(ind1, ind2, sequence):
    sequence = list(map(int, sequence))
    sequence[ind1] *= sequence[ind2]
    return sequence


def decrease(sequence):
    sequence = list(map(int, sequence))
    sequence = [e-1 for e in sequence]
    return sequence


array_values = input().split()
while True:
    command = input().split()
    command_name = command[0]
    if command_name == 'end':
        break
    elif command_name == 'swap':
        index1, index2 = int(command[1]), int(command[2])
        array_values = swap(index1, index2)
    elif command_name == 'multiply':
        index1, index2 = int(command[1]), int(command[2])
        array_values = multiply(index1, index2, array_values)
    elif command_name == 'decrease':
        array_values = decrease(array_values)

print(*array_values, sep=', ')