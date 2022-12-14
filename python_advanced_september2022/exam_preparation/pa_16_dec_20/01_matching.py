from collections import deque

males = deque(int(x) for x in input().split())
females = deque(int(x) for x in input().split())

matches = 0

while males and females:
    if females[0] <= 0:
        females.popleft()
        continue
    if males[-1] <= 0:
        males.pop()
        continue
    if females[0] % 25 == 0:
        females.popleft()
        females.popleft()
        continue
    if males[-1] % 25 == 0:
        males.pop()
        males.pop()
        continue

    female = females.popleft()
    male = males.pop()

    if female == male:
        matches += 1
    elif female != male:
        males.append(male-2)

print(f"Matches: {matches}")
if males:
    males.reverse()
    print(f"Males left: {', '.join(map(str, males))}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print("Females left: none")