a1 = int(input())
a2 = int(input())
n = int(input())
n_devided = int(n / 2)
for char in range(a1, a2):
    ch = chr(char)
    for n1 in range(1, n):
        for n2 in range(1, n_devided):
            n3 = ord(ch)
            if char % 2 != 0:
                if (n1 + n2 + n3) % 2 != 0:
                    print(f"{ch}-{n1}{n2}{n3}")
            else:
                continue