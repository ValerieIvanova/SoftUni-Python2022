import sys

number = int(input())
max_even_num = -sys.maxsize
min_even_num = sys.maxsize
max_odd_num = -sys.maxsize
min_odd_num = sys.maxsize
even_sum = 0
odd_sum = 0

for i in range(1, number + 1):
    num = float(input())
    if i % 2 == 0:
        even_sum += num
        if num > max_even_num:
            max_even_num = num
        if num < min_even_num:
            min_even_num = num
    elif i % 2 != 0:
        odd_sum += num
        if num > max_odd_num:
            max_odd_num = num
        if num < min_odd_num:
            min_odd_num = num

print(f'OddSum={odd_sum:.2f},')
if min_odd_num != sys.maxsize:
    print(f'OddMin={min_odd_num:.2f},')
else:
    print('OddMin=No,')
if max_odd_num != -sys.maxsize:
    print(f'OddMax={max_odd_num:.2f},')
else:
    print('OddMax=No,')
print(f'EvenSum={even_sum:.2f},')
if min_even_num != sys.maxsize:
    print(f'EvenMin={min_even_num:.2f},')
else:
    print('EvenMin=No,')
if max_even_num != -sys.maxsize:
    print(f'EvenMax={max_even_num:.2f}')
else:
    print('EvenMax=No')