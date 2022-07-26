def characters_in_range(a, b):
    list_of_chars = []
    for i in range(ord(a)+1, ord(b)):
        list_of_chars.append(chr(i))
    return list_of_chars
    # return [chr(i) for i in range(ord(a)+1, ord(b)] - list comprehension


start_letter = input()
end_letter = input()
print(' '.join(characters_in_range(start_letter, end_letter)))
# result = characters_in_range(start_letter, end_letter)
# print(*result)