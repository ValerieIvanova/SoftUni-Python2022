list_of_characters = input().split(', ')
dict_of_characters = {i: ord(i) for i in list_of_characters}
print(dict_of_characters)