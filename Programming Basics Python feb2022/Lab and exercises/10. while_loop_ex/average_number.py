n = int(input())
sum = 0
for num in range(n):
    number = int(input())
    sum += number
avr_sum = sum / n
print(f'{avr_sum:.2f}')