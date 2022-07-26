numbers = list(map(int, input().split(', ')))
group = 10
while len(numbers) > 0:
    current_group = []
    for i in range(1, len(numbers)+1):
        if numbers[i-1] != 'none' and numbers[i-1] <= group:
            current_group.append(numbers.pop(i-1))
            numbers.insert(i-1, 'none')
    print(f"Group of {group}'s: {current_group}")
    group += 10
    numbers = [num for num in numbers if num != 'none']