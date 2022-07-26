numbers = list(map(int, input().split()))
avr_value = sum(numbers) / len(numbers)
top_5 = [num for num in numbers if num > avr_value]
if len(top_5) == 0:
    print('No')
else:
    print(*sorted(top_5, reverse=True)[:5])