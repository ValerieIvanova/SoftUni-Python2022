numbers = list(map(int, input().split(', ')))
even_nums_ind = list(map(lambda x: x if numbers[x] % 2 == 0 else None, range(len(numbers))))
index_list = [i for i in even_nums_ind if i is not None]

print(index_list)