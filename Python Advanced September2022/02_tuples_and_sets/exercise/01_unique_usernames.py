lines = int(input())
unique_usernames = set()

for _ in range(lines):
    unique_usernames.add(input())
[print(name) for name in unique_usernames]