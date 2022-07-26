def sum_numbers(first, second):
    return first + second


def subtract(sum, third):
    return sum - third


def add_and_subtract():
    sum_of_first_two_numbers = sum_numbers(first_num, second_num)
    result = subtract(sum_of_first_two_numbers, third_num)
    return result


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(add_and_subtract())