SIZE = 7
players = input().split(', ')

# Player's name: [points, turns]
players_points = {
    players[0]: [501, 0],
    players[1]: [501, 0]
}

dartboard = [input().split() for _ in range(SIZE)]

while True:
    row, col = map(int, input().strip('()').split(', '))
    current_player = players.pop(0)
    players_points[current_player][1] += 1

    if not 0 <= row < SIZE or not 0 <= col < SIZE:
        players.append(current_player)
        continue
    position = dartboard[row][col]
    if position.isdigit():
        players_points[current_player][0] -= int(position)
    elif position == 'D':
        points = (int(dartboard[row][0]) + int(dartboard[row][-1]) + int(dartboard[0][col]) + int(dartboard[-1][col])) * 2
        players_points[current_player][0] -= points
    elif position == 'T':
        points = (int(dartboard[row][0]) + int(dartboard[row][-1]) + int(dartboard[0][col]) + int(dartboard[-1][col])) * 3
        players_points[current_player][0] -= points
    if position == 'B' or players_points[current_player][0] <= 0:
        print(f"{current_player} won the game with {players_points[current_player][1]} throws!")
        break

    players.append(current_player)