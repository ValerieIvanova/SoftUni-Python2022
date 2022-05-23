men = int(input())
women = int(input())
max_tables = int(input())
available_seats = max_tables * 2
for m in range(1, men + 1):
    for w in range(1, women + 1):
        available_seats -= 2
        if available_seats < 0:
            break
        print(f'({m} <-> {w})', end=' ')