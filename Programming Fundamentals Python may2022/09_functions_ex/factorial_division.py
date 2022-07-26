# def factorial(num):
#     for digit in range(1, num):
#         num *= digit
#     return num
#
#
# first_number = int(input())
# second_number = int(input())
# final_result = factorial(first_number) / factorial(second_number)
# print(f'{final_result:.2f}')

from math import factorial
first_num = int(input())
second_num = int(input())
print(f'{factorial(first_num) / factorial(second_num):.2f}')