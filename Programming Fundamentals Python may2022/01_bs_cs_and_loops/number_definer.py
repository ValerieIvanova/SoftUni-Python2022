number = float(input())

if number == 0:
    print('zero')
elif number > 0:
    if abs(number) < 1 and abs(number) != 0:
        print('small', end=' ')
    elif abs(number) > 1000000:
        print('large', end=' ')
    print('positive')
elif number < 0:
    if abs(number) < 1 and abs(number) != 0:
        print('small', end=' ')
    elif abs(number) > 1000000:
        print('large', end=' ')
    print('negative')