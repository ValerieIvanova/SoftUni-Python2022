# input_list = input().split()
# abs_list = [abs(float(n)) for n in input_list]
# print(abs_list)

numbers = list(map(float, input().split()))
result = [abs(num) for num in numbers]
print(result)