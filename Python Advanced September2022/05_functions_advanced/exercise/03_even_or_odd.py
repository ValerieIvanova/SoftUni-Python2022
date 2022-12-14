def even_odd(*args):
    filtered_list = []
    if args[-1] == 'even':
        filtered_list = [x for x in args[:-1] if x % 2 == 0]
    elif args[-1] == 'odd':
        filtered_list = [x for x in args[:-1] if x % 2 != 0]
    return filtered_list


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))