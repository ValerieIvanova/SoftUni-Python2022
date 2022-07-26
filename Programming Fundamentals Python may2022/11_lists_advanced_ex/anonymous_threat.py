strings = input().split()

while True:
    command = input().split()
    command_name = command[0]
    if '3:1' in command:
        print(' '.join(strings))
        break
    if command_name == 'merge':
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
        if end_index >= len(strings):
            end_index = len(strings) - 1
        strings[start_index:end_index + 1] = [''.join(strings[start_index:end_index + 1])]

    elif command_name == 'divide':
        index = int(command[1])
        partitions = int(command[2])
        word = strings[index]
        chars = len(word) // partitions
        new_word = []
        counter = 0
        for i in range(partitions):
            if i == partitions-1:
                new_word.append(word[counter:])
                break
            new_word.append(word[counter:counter + chars])
            counter += chars

        del strings[index]
        for i in range(len(new_word)):
            strings.insert(index + i, new_word[i])