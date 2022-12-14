players = input().split(', ')
maze_board = [input().split() for _ in range(6)]
turn = 0
resting = {players[0]: False, players[1]: False}

while True:
    current_player = players[0]
    row, col = [int(x) for x in input().strip('()').split(', ')]
    position = maze_board[row][col]

    if not resting[current_player]:
        if position == 'E':
            print(f"{current_player} found the Exit and wins the game!")
            break

        elif position == 'T':
            print(f"{current_player} is out of the game! The winner is {players[1]}.")
            break

        elif position == 'W':
            print(f"{current_player} hits a wall and needs to rest.")
            resting[current_player] = True

    else:
        resting[current_player] = False
    players[0], players[1] = players[1], players[0]