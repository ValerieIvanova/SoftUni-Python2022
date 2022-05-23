n = int(input())
l = int(input())
for n1 in range(1, n + 1):
    for n2 in range(1, n + 1):
        # 'a' = 97 (ASCII)
        for char1 in range(97, 97 + l):
            l1 = chr(char1)
            for char2 in range(97, 97 + l):
                l2 = chr(char2)
                for n3 in range(1, n + 1):
                    if n3 > n1 and n3 > n2:
                        print(f'{n1}{n2}{l1}{l2}{n3}', end=' ')