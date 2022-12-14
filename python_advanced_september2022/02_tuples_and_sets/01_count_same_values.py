numbers = tuple(map(float, input().split()))
unique_numbers = []

for item in numbers:
    if item not in unique_numbers:
        print(f'{item} - {numbers.count(item)} times')
        unique_numbers.append(item)