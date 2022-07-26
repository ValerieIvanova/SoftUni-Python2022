current_version = list(map(int, input().split('.')))
current_version[-1] += 1
for current_index in range(len(current_version)-1, -1, -1):
    if current_version[current_index] > 9:
        current_version[current_index] = 0
        if current_index - 1 >= 0:
            current_version[current_index - 1] += 1
print('.'.join(str(s) for s in current_version))

# current_version = input().split('.')
# n1 = int(current_version[0])
# n2 = int(current_version[1])
# n3 = int(current_version[2])
# for _ in range(len(current_version)):
#     if n3 < 9:
#         n3 += 1
#         break
#     else:
#         n3 = 0
#         if n2 < 9:
#             n2 += 1
#             break
#         else:
#             n2 = 0
#             n1 += 1
#             break
# print(f'{n1}.{n2}.{n3}')