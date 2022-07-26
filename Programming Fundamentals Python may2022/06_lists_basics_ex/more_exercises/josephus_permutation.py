circle_of_people = input().split()
kill_count = int(input())
killed = []
counter = 0
index = 0
while len(circle_of_people) > 0:
    counter += 1
    if counter % kill_count == 0:
        killed.append(circle_of_people.pop(index))
    else:
        index += 1

    if index >= len(circle_of_people):
        index = 0

print(f"[{','.join(killed)}]")