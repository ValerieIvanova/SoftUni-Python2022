list_of_integers_str = input().split()
count_of_numbers_to_remove = int(input())
list_of_integers = [int(i) for i in list_of_integers_str]
the_biggest = []
for i in range(count_of_numbers_to_remove):
    list_of_integers.remove(min(list_of_integers))
list_of_integers_str = [str(i) for i in list_of_integers]
print(', '.join(list_of_integers_str))