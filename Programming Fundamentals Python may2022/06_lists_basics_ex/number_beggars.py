string = input().split(', ')
beggars = int(input())
index_counter = 0
final_list = []
digits_list = [int(i) for i in string]
while index_counter < beggars:
    temp_sum = 0
    for j in range(index_counter, len(digits_list), beggars):
        temp_sum += digits_list[j]
    final_list.append(temp_sum)
    index_counter += 1
print(final_list)