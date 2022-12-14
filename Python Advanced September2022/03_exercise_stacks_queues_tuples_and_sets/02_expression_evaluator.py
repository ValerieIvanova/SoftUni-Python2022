from functools import reduce

expression = input().split()
stack = []
for el in expression:
    if el.lstrip('-').isdigit():  # lstrip() in case it's a negative number
        stack.append(int(el))
    else:
        if el == '*':
            stack = [reduce(lambda x, y: x * y, stack)]
        elif el == '/':
            stack = [reduce(lambda x, y: x // y, stack)]
        elif el == '+':
            stack = [reduce(lambda x, y: x + y, stack)]
        elif el == '-':
            stack = [reduce(lambda x, y: x - y, stack)]

print(stack[0])