moves = int(input())
zero_to_9 = 0
ten_to_19 = 0
twenty_to_29 = 0
thirty_to_39 = 0
forty_to_50 = 0
invalid_number = 0
result = 0
for n in range(moves):
    num = int(input())
    if 0 <= num <= 9:
        result += num * 0.2
        zero_to_9 += 1
    elif 10 <= num <= 19:
        result += num * 0.3
        ten_to_19 += 1
    elif 20 <= num <= 29:
        result += num * 0.4
        twenty_to_29 += 1
    elif 30 <= num <= 39:
        result += 50
        thirty_to_39 += 1
    elif 40 <= num <= 50:
        result += 100
        forty_to_50 += 1
    else:
        result = result / 2
        invalid_number += 1
zero_to_9_percent = zero_to_9 / moves * 100
ten_to_19_percent = ten_to_19 / moves * 100
twenty_to_29_percent = twenty_to_29 / moves * 100
thirty_to_39_percent = thirty_to_39 / moves * 100
forty_to_50_percent = forty_to_50 / moves * 100
invalid_number_percent = invalid_number / moves * 100
print(f'{result:.2f}')
print(f'From 0 to 9: {zero_to_9_percent:.2f}%')
print(f'From 10 to 19: {ten_to_19_percent:.2f}%')
print(f'From 20 to 29: {twenty_to_29_percent:.2f}%')
print(f'From 30 to 39: {thirty_to_39_percent:.2f}%')
print(f'From 40 to 50: {forty_to_50_percent:.2f}%')
print(f'Invalid numbers: {invalid_number_percent:.2f}%')