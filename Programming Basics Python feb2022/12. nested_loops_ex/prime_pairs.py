first_num_starting_value = int(input())
second_num_starting_value = int(input())
first_num_diff = int(input())
second_num_diff = int(input())
first_num_end_value = first_num_starting_value + first_num_diff
second_num_end_value = second_num_starting_value + second_num_diff

for n1 in range(first_num_starting_value, first_num_end_value + 1):
    prime1 = True
    for i in range(2, n1):
        if n1 % i == 0:
            prime1 = False
            continue
    for n2 in range(second_num_starting_value, second_num_end_value + 1):
        prime2 = True
        for j in range(2, n2):
            if n2 % j == 0:
                prime2 = False
                continue
        if prime1 and prime2:
            print(f'{n1}{n2}')