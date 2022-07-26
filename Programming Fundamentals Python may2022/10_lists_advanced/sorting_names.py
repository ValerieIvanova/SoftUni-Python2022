names = input().split(', ')
# Sorting with two keys
# sorted_names_length = sorted(names, key=lambda x: (-len(x), x))
sorted_names_alpha = sorted(names)
sorted_names_length = sorted(sorted_names_alpha, key=lambda name: -len(name))
print(sorted_names_length)