num1 = int(input())
num2 = int(input())

for num in range(num1, num2 + 1):
    odd_sum = 0
    even_sum = 0
    for current_num in range(len(str(num))):
        if current_num % 2 == 0:
            even_sum += int(str(num)[current_num])
        else:
            odd_sum += int(str(num)[current_num])
    if even_sum == odd_sum:
        print(num, end=' ')
        