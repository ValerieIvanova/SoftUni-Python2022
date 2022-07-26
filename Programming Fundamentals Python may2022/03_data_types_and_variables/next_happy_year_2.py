from itertools import permutations

number = tuple(map(int, input()))
myperm = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], len(number))
for digits in list(myperm):
    if digits > number:
        result = ''.join(str(x) for x in digits)
        print(result)
        break