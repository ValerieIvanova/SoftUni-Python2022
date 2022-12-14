n, m = map(int, input().split())
first_set = set()
second_set = set()

for _ in range(n):
    first_set.add(int(input()))
for _ in range(m):
    second_set.add(int(input()))

print(*first_set.intersection(second_set), sep='\n')