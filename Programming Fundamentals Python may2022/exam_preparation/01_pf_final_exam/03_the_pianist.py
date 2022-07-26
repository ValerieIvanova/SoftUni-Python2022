def add_pieces(piece_, composer_, key_):
    if piece_ not in pieces_dict:
        pieces_dict[piece_] = [composer_, key_]
        return f"{piece_} by {composer_} in {key_} added to the collection!"
    else:
        return f"{piece_} is already in the collection!"


def remove_piece(piece_):
    if piece_ not in pieces_dict:
        return f"Invalid operation! {piece_} does not exist in the collection."
    del pieces_dict[piece_]
    return f"Successfully removed {piece_}!"


def change_key(piece_, new_key_):
    if piece_ not in pieces_dict:
        return f"Invalid operation! {piece_} does not exist in the collection."
    pieces_dict[piece][1] = new_key
    return f"Changed the key of {piece_} to {new_key_}!"


number_of_pieces = int(input())
pieces_dict = {}
for i in range(number_of_pieces):
    pieces_info = input().split('|')
    pieces_dict[pieces_info[0]] = [pieces_info[1], pieces_info[2]]

while True:
    command = input().split('|')
    command_name = command[0]
    if command_name == 'Stop':
        break
    elif command_name == 'Add':
        piece, composer, key = command[1:]
        print(add_pieces(piece, composer, key))
    elif command_name == 'Remove':
        piece = command[1]
        print(remove_piece(piece))
    elif command_name == 'ChangeKey':
        piece = command[1]
        new_key = command[2]
        print(change_key(piece, new_key))

for piece, info in pieces_dict.items():
    print(f"{piece} -> Composer: {info[0]}, Key: {info[1]}")

# Print with comprehension:
# [print(f"{piece} -> Composer: {info[0]}, Key: {info[1]}") for piece, info in pieces_dict.items()]
