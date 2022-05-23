floors = int(input())
rooms_per_floor = int(input())
room_number = 0
room_name = ''

for floor in range(floors, 0, -1):
    for n in range(rooms_per_floor):
        room_number = floor * 10 + n
        if floor == floors:
            room_name = f'L{room_number} '
        elif floor % 2 != 0:
            room_name = f'A{room_number} '
        elif floor % 2 == 0:
            room_name = f'O{room_number} '

        print(room_name, end='')
    print()