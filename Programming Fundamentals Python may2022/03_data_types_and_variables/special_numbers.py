n = int(input())
for num in range(1, n + 1):
    number = num
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number = number // 10
    is_special = digit_sum == 5 or digit_sum == 7 or digit_sum == 11
    print(f'{num} -> {is_special}')