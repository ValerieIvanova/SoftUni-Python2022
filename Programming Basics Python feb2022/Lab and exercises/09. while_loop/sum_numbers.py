start_sum = int(input())
second_sum = 0
while True:
    current_sum = int(input())
    second_sum += current_sum
    if second_sum >= start_sum:
        print(second_sum)
        break