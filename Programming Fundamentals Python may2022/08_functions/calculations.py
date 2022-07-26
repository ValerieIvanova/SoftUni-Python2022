# def calculator(a, b, operator):
#     result = None
#     if operator == 'multiply':
#         result = a * b
#     elif operator == 'divide':
#         result = int(a / b)
#     elif operator == 'add':
#         result = a + b
#     elif operator == 'subtract':
#         result = a - b
#     return result
#
#
# current_operator = input()
# first_num = int(input())
# second_num = int(input())
# print(calculator(first_num, second_num, current_operator))

import operator


def calculations(a, b, operation):
    operations_dict = {'multiply': operator.mul,
                       'divide': operator.truediv,
                       'add': operator.add,
                       'subtract': operator.sub}
    return int(operations_dict[operation](a, b))


type_of_operation = input()
first_num = int(input())
second_num = int(input())
print(calculations(first_num, second_num, type_of_operation))