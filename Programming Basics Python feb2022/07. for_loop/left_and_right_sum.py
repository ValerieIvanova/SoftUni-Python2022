n = int(input())

left_sum = 0
right_sum = 0

for num in range(n):
    num1 = int(input())
    left_sum += num1
for num in range(n):
    num2 = int(input())
    right_sum += num2

diff = abs(left_sum - right_sum)

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {diff}')