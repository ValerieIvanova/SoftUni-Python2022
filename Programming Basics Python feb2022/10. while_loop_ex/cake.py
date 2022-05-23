width = int(input())
length = int(input())
number_of_pieces = int((width / 1) * (length / 1))
pieces_taken = 0
diff = 0
while True:
    current_pieces = input()
    if current_pieces == 'STOP':
        diff = abs(number_of_pieces - pieces_taken)
        print(f'{diff} pieces are left.')
        break

    pieces_taken += int(current_pieces)

    if pieces_taken >= number_of_pieces:
        diff = abs(number_of_pieces - pieces_taken)
        print(f'No more cake left! You need {diff} pieces more.')
        break