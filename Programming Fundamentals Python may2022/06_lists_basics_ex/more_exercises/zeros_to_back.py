numbers_str = input().split(', ')
numbers = [int(n) for n in numbers_str if int(n) != 0]
numbers += [int(zero) for zero in numbers_str if int(zero) == 0]
print(numbers)