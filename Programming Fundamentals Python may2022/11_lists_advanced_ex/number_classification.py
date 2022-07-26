# numbers = [int(num) for num in input().split(', ')]
# positive_numbers = [str(p) for p in numbers if p >= 0]
# negative_numbers = [str(n) for n in numbers if n < 0]
# even_numbers = [str(e) for e in numbers if e % 2 == 0]
# odd_numbers = [str(o) for o in numbers if o % 2 != 0]
#
# print(f"Positive: {', '.join(positive_numbers)}\n"
#       f"Negative: {', '.join(negative_numbers)}\n"
#       f"Even: {', '.join(even_numbers)}\n"
#       f"Odd: {', '.join(odd_numbers)}")


# Another way with functions:
def positive_numbers(number):
    return [str(p) for p in number if p >= 0]


def negative_numbers(number):
    return [str(n) for n in number if n < 0]


def even_numbers(number):
    return [str(e) for e in number if e % 2 == 0]


def odd_numbers(number):
    return [str(o) for o in number if o % 2 != 0]


numbers = [int(num) for num in input().split(', ')]
print(f"Positive: {', '.join(positive_numbers(numbers))}\n"
      f"Negative: {', '.join(negative_numbers(numbers))}\n"
      f"Even: {', '.join(even_numbers(numbers))}\n"
      f"Odd: {', '.join(odd_numbers(numbers))}")