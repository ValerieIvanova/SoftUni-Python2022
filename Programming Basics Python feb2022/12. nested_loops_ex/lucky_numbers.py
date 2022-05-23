n = int(input())

for n1 in range(1, n + 1):
    for n2 in range(1, n + 1):
        for n3 in range(1, n + 1):
            for n4 in range(1, n + 1):
                if n1 + n2 == n3 + n4:
                    if n % (n1 + n2) == 0:
                        if n1 > 9 or n2 > 9 or n3 > 9 or n4 > 9:
                            break
                        print(f'{n1}{n2}{n3}{n4}', end=' ')