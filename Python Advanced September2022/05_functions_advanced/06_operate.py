from functools import reduce


def operate(operator, *args):
    result = None
    if operator == '+':
        result = reduce(lambda x, y: x + y, args)
    elif operator == '-':
        result = reduce(lambda x, y: x - y, args)
    elif operator == '*':
        result = reduce(lambda x, y: x * y, args)
    elif operator == '/':
        result = reduce(lambda x, y: x / y, args)
    return result


print(operate("*", 3, 4))
print(operate("+", 1, 2, 3))
print(operate('-', 5, 4, 1))
print(operate('/', 6, 2))
