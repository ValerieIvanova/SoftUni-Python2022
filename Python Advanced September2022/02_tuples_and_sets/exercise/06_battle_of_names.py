lines = int(input())
set_even = set()
set_odd = set()

for row in range(1, lines+1):
    name = input()
    sum_ascii = 0
    for char in name:
        sum_ascii += ord(char)

    sum_ascii //= row
    if sum_ascii % 2 == 0:
        set_even.add(sum_ascii)
    else:
        set_odd.add(sum_ascii)

sum_even = sum(set_even)
sum_odd = sum(set_odd)
if sum_even == sum_odd:
    print(*set_odd.union(set_even), sep=', ')
if sum_odd > sum_even:
    print(*set_odd.difference(set_even), sep=', ')
else:
    print(*set_odd.symmetric_difference(set_even), sep=', ')