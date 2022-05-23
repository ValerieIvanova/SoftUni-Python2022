start = input()
end = input()

for n1 in range(int(start[0]), int(end[0]) + 1):
    for n2 in range(int(start[1]), int(end[1]) + 1):
        for n3 in range(int(start[2]), int(end[2]) + 1):
            for n4 in range(int(start[3]), int(end[3]) + 1):
                if n1 % 2 != 0 and n2 % 2 != 0 and n3 % 2 != 0 and n4 % 2 != 0:
                    print(f'{n1}{n2}{n3}{n4}', end=' ')
                else:
                    continue