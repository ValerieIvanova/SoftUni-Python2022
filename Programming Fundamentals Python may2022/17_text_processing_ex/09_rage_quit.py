def unique_symbols(symbol, symbols):
    if symbol.lower() not in symbols:
        symbols.append(symbol.lower())
    return symbols


string = input()
repeats = ''
message = ''
current_message = ''
unique_symbols_list = []
for i in range(len(string)):
    if not string[i].isdigit():
        unique_symbols(string[i], unique_symbols_list)
        current_message += string[i]
    else:
        for j in range(i, len(string)):
            if not string[j].isdigit():
                break
            repeats += string[j]
        message += current_message.upper() * int(repeats)
        current_message = ''
        repeats = ''

print(f'Unique symbols used: {len(unique_symbols_list)}')
print(message)