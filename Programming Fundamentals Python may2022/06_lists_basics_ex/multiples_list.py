factor = int(input())
count = int(input())
numbers_list = []
for i in range(1, count + 1):
    numbers_list.append(factor * i)
print(numbers_list)