# divisor = int(input())
# boundary = int(input())
# max_num = 0
# for num in range(1, boundary + 1):
#     if num % divisor == 0:
#         max_num = num
# print(max_num)

divisor = int(input())
boundary = int(input())
max_num = 0
for num in range(boundary, divisor, -1):
    if num % divisor == 0:
        max_num = num
        break
print(max_num)