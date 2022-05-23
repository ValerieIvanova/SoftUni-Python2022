import sys
number = input()
min_number = sys.maxsize
while number != 'Stop':
    num = int(number)
    if num < min_number:
        min_number = num
    number = input()
print(min_number)