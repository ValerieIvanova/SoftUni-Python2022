M = int(input())
found = False
combinations = 0
password = f''
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if ((a * b) + (c * d)) == M:
                    if a < b and c > d:
                        combinations += 1
                        print(f'{a}{b}{c}{d}', end=' ')
                        if combinations == 4:
                            found = True
                            password = f"{a}{b}{c}{d}"
if not found:
    if combinations == 0:
        print('No!')
    else:
        print()
        print('No!')
else:
    print()
    print(f'Password: {password}')