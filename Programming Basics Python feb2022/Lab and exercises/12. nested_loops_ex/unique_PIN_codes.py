n1_limit = int(input())
n2_limit = int(input())
n3_limit = int(input())
is_prime = False
first_n = 0
second_n = 0
third_n = 0
for n1 in range(1, n1_limit + 1):
    if n1 % 2 == 0:
        first_n = n1
        for n2 in range(2, n2_limit + 1):
            is_prime = True
            for i in range(2, n2):
                if n2 % i == 0:
                    is_prime = False
                    break
            if not is_prime:
                continue
            else:
                second_n = n2
                for n3 in range(1, n3_limit + 1):
                    if n3 % 2 == 0:
                        third_n = n3
                        print(f'{first_n} {second_n} {third_n}')
    continue