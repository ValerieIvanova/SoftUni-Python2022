import sys

n = int(input())
max_num = -sys.maxsize
current_sum = 0

for num in range(n):
    current_number = int(input())
    if current_number > max_num:
        max_num = current_number

    current_sum += current_number

if (current_sum - max_num) == max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    diff = abs((current_sum - max_num) - max_num)
    print('No')
    print(f'Diff = {diff}')