n = float(input())

while n >= 0:
    result = n * 2
    print(f'Result: {result:.2f}')
    n = float(input())
if not n >= 0:
    print('Negative number!')
