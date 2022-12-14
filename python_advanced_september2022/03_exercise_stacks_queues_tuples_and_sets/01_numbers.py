# first_set = set(map(int, input().split()))
# second_set = set(map(int, input().split()))
first_set, second_set = {*input().split()}, {*input().split()}
n = int(input())
for _ in range(n):
    command = input().split(' ', 2)
    if command[0] == 'Add':
        if command[1] == 'First':
            [first_set.add(int(num)) for num in command[2].split()]
        elif command[1] == 'Second':
            [second_set.add(int(num)) for num in command[2].split()]

    elif command[0] == 'Remove':
        if command[1] == 'First':
            [first_set.discard(int(num)) for num in command[2].split()]
        elif command[1] == 'Second':
            [second_set.discard(int(num)) for num in command[2].split()]

    elif command[0] == 'Check':
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')