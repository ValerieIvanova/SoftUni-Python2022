elements_sequence = input().split()
moves = 0

while True:
    command = input()
    if command == 'end':
        print('Sorry you lose :(')
        print(' '.join(elements_sequence))
        break
    indexes = command.split()
    first_index = int(indexes[0])
    second_index = int(indexes[1])
    moves += 1
    if (first_index == second_index) \
            or (first_index < 0 or first_index >= len(elements_sequence)) \
            or (second_index < 0 or second_index >= len(elements_sequence)):
        middle_of_the_sequence = len(elements_sequence) // 2
        elements_sequence.insert(middle_of_the_sequence, f'-{moves}a')
        elements_sequence.insert(middle_of_the_sequence, f'-{moves}a')
        print("Invalid input! Adding additional elements to the board")

    elif elements_sequence[first_index] == elements_sequence[second_index]:
        print(f"Congrats! You have found matching elements - {elements_sequence[first_index]}!")
        elements_sequence[first_index] = 'None'
        elements_sequence[second_index] = 'None'
    elif elements_sequence[first_index] != elements_sequence[second_index]:
        print('Try again!')

    elements_sequence = [element for element in elements_sequence if element != 'None']
    if len(elements_sequence) == 0:
        print(f'You have won in {moves} turns!')
        break
