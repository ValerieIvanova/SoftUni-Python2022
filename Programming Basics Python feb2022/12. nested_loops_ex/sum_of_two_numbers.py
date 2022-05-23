start = int(input())
end = int(input())
magic_number = int(input())
combinations = 0
sum = 0
flag = False
for n1 in range(start, end + 1):
    for n2 in range(start, end + 1):
        combinations += 1
        sum = n1 + n2
        if sum == magic_number:
            flag = True
            print(f'Combination N:{combinations} ({n1} + {n2} = {magic_number})')
            break
        else:
            continue
    if flag:
        break
    elif not flag:
        continue
if not flag:
    print(f'{combinations} combinations - neither equals {magic_number}')
