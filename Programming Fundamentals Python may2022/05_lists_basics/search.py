number_of_lines = int(input())
word = input()
strings_list = []
new_list = []
for i in range(number_of_lines):
    string = input()
    strings_list.append(string)
    if word in string:
        new_list.append(string)
print(strings_list)
print(new_list)