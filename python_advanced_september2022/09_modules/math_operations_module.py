def add(a, b):
    return f"{a + b:.2f}"


def sub(a, b):
    return f"{a - b:.2f}"


def mul(a, b):
    return f"{a * b:.2f}"


def div(a, b):
    return f"{a / b:.2f}"


def raise_nums(a, b):
    return f"{a ** b:.2f}"


def calculate(a, b, op):
    if op == '+':
        return add(a, b)
    elif op == '-':
        return sub(a, b)
    elif op == '/':
        return div(a, b)
    elif op == '*':
        return mul(a, b)
    elif op == '^':
        return raise_nums(a, b)
    raise ValueError('Not supported operation')


def calculate_expression(expression):
    first, operator, second = expression.split()
    return calculate(float(first), int(second), operator)
