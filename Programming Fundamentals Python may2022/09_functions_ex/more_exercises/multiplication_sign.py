def multiplication_sign(numbers_list):
    negative_count = 0
    positive = True
    negative = False
    zero = False
    for s in numbers_list:
        if s < 0 and not zero:
            negative_count += 1
            if negative_count % 2 != 0:
                positive = False
                negative = True
            else:
                positive = True
                negative = False
        elif s == 0:
            positive = False
            negative = False
            zero = True
    if zero:
        return 'zero'
    elif negative:
        return 'negative'
    elif positive:
        return 'positive'


num1 = int(input())
num2 = int(input())
num3 = int(input())
numbers = [num1, num2, num3]
print(multiplication_sign(numbers))