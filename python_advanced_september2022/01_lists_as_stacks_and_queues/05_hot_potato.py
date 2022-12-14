from collections import deque

names = deque(input().split())
toss = int(input())
counter = 1
while len(names) > 1:
    kid = names.popleft()
    if counter == toss:
        print(f"Removed {kid}")
        counter = 1
    else:
        counter += 1
        names.append(kid)
winner = names.popleft()
print(f"Last is {winner}")
