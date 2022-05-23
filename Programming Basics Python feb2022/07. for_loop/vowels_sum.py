word = input()
sum = 0

for ch in word:
    if ch == 'a':
        sum += 1
    if ch == 'e':
        sum += 2
    if ch == 'i':
        sum += 3
    if ch == 'o':
        sum += 4
    if ch == 'u':
        sum += 5

print(sum)