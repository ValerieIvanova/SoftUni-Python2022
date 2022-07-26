# 1:

# from collections import defaultdict
#
# rss_dict = defaultdict(int)
#
# while True:
#     command = input()
#     if command == 'stop':
#         break
#     resource = command
#     quantity = int(input())
#     rss_dict[resource] += quantity
#
# for r, q in rss_dict.items():
#     print(f'{r} -> {q}')

# 2------------------------------------:

resources = {}
line = 0
while True:
    command = input()
    if command == 'stop':
        break
    resource = command
    quantity = int(input())
    if resource not in resources:
        resources[resource] = quantity
    resources[resource] += quantity
[print(f"{r} -> {q}") for r, q in resources.items()]