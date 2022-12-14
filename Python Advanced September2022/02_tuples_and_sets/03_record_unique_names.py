lines = int(input())
names = [input() for _ in range(lines)]
[print(name) for name in set(names)]

# lines = int(input())
# names = set()
# for i in range(lines):
#     names.add(input())
# [print(name) for name in names]