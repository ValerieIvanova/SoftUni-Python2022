string = input()
numbers_list = [num for num in string if num.isdigit()]
string_list = [element for element in string if not element.isdigit()]
take_list = [int(numbers_list[i]) for i in range(len(numbers_list)) if i % 2 == 0]
skip_list = [int(numbers_list[i]) for i in range(len(numbers_list)) if i % 2 != 0]
take_number = 0
skip_number = 0
result_string = ''
for i in range(len(take_list)):
    take_number = take_list[i]
    skip_number = skip_list[i]
    result_string += ''.join(string_list[:take_number])
    del string_list[0:take_number + skip_number]
print(result_string)