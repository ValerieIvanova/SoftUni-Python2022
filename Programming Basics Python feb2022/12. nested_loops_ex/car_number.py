start = int(input())
end = int(input())

for n1 in range(start, end + 1):
    for n2 in range(start, end + 1):
        for n3 in range(start, end + 1):
            for n4 in range(start, end + 1):
                if n1 % 2 == 0 and n4 % 2 == 0:
                    continue
                if n1 % 2 != 0 and n4 % 2 != 0:
                    continue
                if n1 < n4:
                    continue
                if (n2 + n3) % 2 == 0:
                    print(f'{n1}{n2}{n3}{n4}', end=' ')