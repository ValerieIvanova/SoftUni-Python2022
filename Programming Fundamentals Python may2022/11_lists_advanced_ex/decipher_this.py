message = input().split()
final_message = []
for word in message:
    current_word = []
    final_word = ''
    numeric_char = ''
    counter = 0
    for char in word:
        if char.isdigit():
            numeric_char += char
            continue
        elif char.isalpha():
            current_word.append(char)
            continue

    current_word[0], current_word[-1] = current_word[-1], current_word[0]
    final_word += chr(int(numeric_char))
    final_word += ''.join(current_word)
    final_message.append(final_word)

print(' '.join(final_message))
