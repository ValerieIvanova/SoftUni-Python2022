from collections import deque

pizza_orders = deque(int(x) for x in input().split(', ') if 0 < int(x) <= 10)
employees = deque(int(x) for x in input().split(', '))
total_pizzas = 0

while pizza_orders and employees:
    order = pizza_orders.popleft()
    employee = employees.pop()
    if order <= employee:
        total_pizzas += order
    elif order > employee:
        order -= employee
        total_pizzas += employee
        pizza_orders.appendleft(order)

if not pizza_orders:
    print(f"All orders are successfully completed!\n"
          f"Total pizzas made: {total_pizzas}\n"
          f"Employees: {', '.join(map(str, employees))}")
elif pizza_orders and not employees:
    print(f"Not all orders are completed.\n"
          f"Orders left: {', '.join(map(str, pizza_orders))}")