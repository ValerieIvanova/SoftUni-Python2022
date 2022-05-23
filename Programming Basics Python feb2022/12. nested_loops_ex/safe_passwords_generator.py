a = int(input())
b = int(input())
max_passwords = int(input())
combinations = 0
flag = False
for s1 in range(35, 55):
    for s2 in range(64, 96):
        for s3 in range(1, a + 1):
            for s4 in range(1, b + 1):
                combinations += 1
                if combinations > max_passwords:
                    flag = True
                    break
                print(f'{chr(s1)}{chr(s2)}{s3}{s4}{chr(s2)}{chr(s1)}', end='|')
                if s3 == a and s4 == b:
                    flag = True
                    break
                s1 += 1
                if s1 > 55:
                    s1 = 35
                s2 += 1
                if s2 > 96:
                    s2 = 64
            if flag:
                break
        if flag:
            break
    if flag:
        break