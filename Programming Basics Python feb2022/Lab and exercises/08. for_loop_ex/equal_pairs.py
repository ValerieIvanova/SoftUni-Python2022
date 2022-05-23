n = int(input())
num1 = int(input())
num2 = int(input())
result = num1 + num2
diff = 0
condition = True

for num in range(n - 1):
    current_num1 = int(input())
    current_num2 = int(input())
    current_result = current_num1 + current_num2
    if current_result != result:
        condition = False
        diff = abs(result - current_result)
        result = current_result
if condition:
    print(f'Yes, value={result}')
else:
    print(f'No, maxdiff={diff}')