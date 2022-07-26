rooms = int(input())
total_free_chairs = 0
not_enough = False
for i in range(1, rooms + 1):
    info = input().split()
    chairs = info[0]
    visitors = int(info[1])
    if visitors > len(chairs):
        chairs_needed = visitors - len(chairs)
        print(f'{chairs_needed} more chairs needed in room {i}')
        not_enough = True
    else:
        total_free_chairs += len(chairs) - visitors
if not not_enough:
    print(f'Game On, {total_free_chairs} free chairs left')