from collections import deque

queue = deque()
while True:
    command = input()
    if command == 'End':
        print(f"{len(queue)} people remaining.")
        break
    elif command == 'Paid':
        print('\n'.join(queue))
        queue.clear()
        continue
    queue.append(command)
