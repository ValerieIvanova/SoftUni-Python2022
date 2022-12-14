def get_primes(integers):
    for num in integers:
        if num <= 1:
            continue
        for number in range(2, num):
            if num % number == 0:
                break
        else:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))