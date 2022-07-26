n = int(input())
for symbol_1 in range(n):
    for symbol_2 in range(n):
        for symbol_3 in range(n):
            # "a" from ascii = 97
            print(f'{chr(97 + symbol_1)}{chr(97 + symbol_2)}{chr(97 + symbol_3)}')