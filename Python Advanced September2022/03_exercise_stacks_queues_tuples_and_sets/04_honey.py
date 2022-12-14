from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
operators = deque(input().split())

total_honey = 0

while bees and nectar:
    if nectar[-1] >= bees[0]:
        symbol = operators.popleft()
        collected_nectar, bee = nectar.pop(), bees.popleft()
        if symbol == '+':
            total_honey += abs(bee + collected_nectar)
        elif symbol == '-':
            total_honey += abs(bee - collected_nectar)
        elif symbol == '*':
            total_honey += abs(bee * collected_nectar)
        elif symbol == '/':
            if collected_nectar == 0 or bee == 0:
                continue
            total_honey += abs(bee / collected_nectar)

    else:
        nectar.pop()
print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")