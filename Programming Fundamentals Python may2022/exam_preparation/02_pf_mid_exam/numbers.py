numbers = list(map(int, input().split()))
avr_value = sum(numbers) / len(numbers)
top_5 = []
for num in numbers:
    if num > avr_value:
        top_5.append(num)

if len(top_5) <= 0:
    print('No')
else:
    print(*sorted(top_5, reverse=True)[:5])