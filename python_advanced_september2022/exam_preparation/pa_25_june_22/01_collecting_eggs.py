from collections import deque

eggs = deque(int(x) for x in input().split(', '))
paper = deque(int(x) for x in input().split(', '))
boxes = 0

while eggs and paper:
    current_egg = eggs.popleft()
    current_paper = paper[-1]
    if current_egg <= 0:
        continue
    elif current_egg == 13:
        paper[0], paper[-1] = paper[-1], paper[0]
        continue
    elif current_egg + current_paper <= 50:
        boxes += 1
    paper.pop()

if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join(map(str, eggs))}")
if paper:
    print(f"Pieces of paper left: {', '.join(map(str, paper))}")