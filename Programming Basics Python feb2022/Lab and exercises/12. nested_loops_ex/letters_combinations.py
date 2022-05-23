letter_start = input()
letter_end = input()
letter_skip = input()

combinations = 0

for ch1 in range(ord(letter_start), ord(letter_end) + 1):
    if chr(ch1) == letter_skip:
        continue
    for ch2 in range(ord(letter_start), ord(letter_end) + 1):
        if chr(ch2) == letter_skip:
            continue
        for ch3 in range(ord(letter_start), ord(letter_end) + 1):
            if chr(ch3) == letter_skip:
                continue
            print(f'{chr(ch1)}{chr(ch2)}{chr(ch3)}', end=' ')
            combinations += 1
print(combinations)