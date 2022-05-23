word = ''
sentence = ''
c = 0
o = 0
n = 0
while True:
    symbol = input()
    if symbol == 'End':
        break
    if symbol == 'c' and c == 0:
        c += 1
    elif symbol == 'o' and o == 0:
        o += 1
    elif symbol == 'n' and n == 0:
        n += 1
    elif symbol.isalpha():
        word += symbol

    if c == 1 and o == 1 and n == 1:
        sentence += word
        sentence += ' '
        word = ''
        c = 0
        o = 0
        n = 0
print(sentence)