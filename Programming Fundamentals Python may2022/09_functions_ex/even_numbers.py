numbers = list(map(int, input().split()))
result = list(filter(lambda x: x % 2 == 0, numbers))
# is_even = lambda x: x % 2 == 0
# result = list(filter(is_even, numbers))
print(result)