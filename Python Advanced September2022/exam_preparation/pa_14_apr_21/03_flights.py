def flights(*args):
    destinations_info = {}
    for i in range(len(args)):
        if args[i] == 'Finish':
            break
        elif i % 2 == 0:
            if args[i] not in destinations_info:
                destinations_info[args[i]] = 0
        else:
            destinations_info[args[i-1]] += int(args[i])

    return destinations_info


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))