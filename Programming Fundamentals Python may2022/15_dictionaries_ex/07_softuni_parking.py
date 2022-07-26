def register(username_, license_plate_):
    if username_ in parking_validator:
        return f"ERROR: already registered with plate number {parking_validator[username_]}"
    else:
        parking_validator[username_] = license_plate_
        return f"{username_} registered {license_plate_} successfully"


def unregister(username_):
    if username_ not in parking_validator:
        return f"ERROR: user {username_} not found"
    else:
        del parking_validator[username_]
        return f"{username_} unregistered successfully"


number_of_commands = int(input())
parking_validator = {}
for c in range(number_of_commands):
    command = input().split()
    if command[0] == 'register':
        username, license_plate = command[1], command[2]
        print(register(username, license_plate))

    elif command[0] == 'unregister':
        username = command[1]
        print(unregister(username))

[print(f"{user} => {license_p}") for user, license_p in parking_validator.items()]