k = int(input())
l = int(input())
m = int(input())
n = int(input())
combinations = 0
max_combinations = False
for n11 in range(k, 8 + 1):
    for n12 in range(9, l - 1, -1):
        for n21 in range(m, 8 + 1):
            for n22 in range(9, n - 1, -1):
                if n11 % 2 == 0 and n21 % 2 == 0 and n12 % 2 != 0 and n22 % 2 != 0:
                    if n11 == n21 and n12 == n22:
                        print('Cannot change the same player.')
                    else:
                        combinations += 1
                        if combinations == 6:
                            max_combinations = True
                            print(f'{n11}{n12} - {n21}{n22}')
                            break
                        else:
                            print(f'{n11}{n12} - {n21}{n22}')
            if max_combinations:
                break
        if max_combinations:
            break
    if max_combinations:
        break