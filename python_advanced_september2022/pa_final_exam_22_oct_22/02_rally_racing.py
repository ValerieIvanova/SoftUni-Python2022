def moves(r, c, command_):
    global total_km, finished
    new_r = r + directions[command_][0]
    new_c = c + directions[command_][1]
    position = route[new_r][new_c]

    if position == '.':
        total_km += 10

    elif position == 'T':
        route[new_r][new_c] = '.'
        end_of_tunnel = False
        for i in range(new_r, size):
            for j in range(size):
                if route[i][j] == "T":
                    route[i][j] = '.'
                    new_r = i
                    new_c = j
                    total_km += 30
                    end_of_tunnel = True
                    break
            if end_of_tunnel:
                break

    elif position == 'F':
        total_km += 10
        finished = True
        print(f"Racing car {tracked_car_number} finished the stage!")

    return new_r, new_c


size = int(input())
tracked_car_number = input()
route = [input().split() for _ in range(size)]
car_pos = [0, 0]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

total_km = 0
finished = False

while True:
    if finished:
        break

    command = input()

    if command == 'End':
        print(f"Racing car {tracked_car_number} DNF.")
        break

    row, col = car_pos[0], car_pos[1]
    car_pos[0], car_pos[1] = moves(row, col, command)

print(f"Distance covered {total_km} km.")
route[car_pos[0]][car_pos[1]] = 'C'
[print(*row, sep='') for row in route]