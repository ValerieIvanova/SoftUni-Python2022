from collections import deque

food_quantity = int(input())
orders = deque(map(int, input().split()))
print(max(orders))
while orders:
    if food_quantity >= orders[0]:
        food_quantity -= orders.popleft()
    else:
        break
if orders:
    print(f"Orders left:", *orders, sep=" ")
else:
    print("Orders complete")