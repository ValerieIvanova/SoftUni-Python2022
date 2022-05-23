first_num_limit = int(input())
second_num_limit = int(input())
third_num_limit = int(input())
prime = False
for n1 in range(1, first_num_limit + 1):
    if n1 % 2 != 0:
        continue

    for n2 in range(2, second_num_limit + 1):
        prime = True
        for i in range(2, n2):
            if n2 % i == 0:
                prime = False
                break
        if not prime:
            continue
        else:
            for n3 in range(1, third_num_limit + 1):
                if n3 % 2 != 0:
                    continue
                print(f'{n1} {n2} {n3}')