def perfect_number(num):
    positive_divisors = []
    for digit in range(1, num):
        if num % digit == 0:
            positive_divisors.append(digit)
    if sum(positive_divisors) == num:
        return 'We have a perfect number!'
    return "It's not so perfect."


number = int(input())
print(perfect_number(number))
