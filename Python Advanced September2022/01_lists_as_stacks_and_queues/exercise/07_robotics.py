from collections import deque


def convert_str_to_seconds(str_time):
    hours, minutes, seconds = [int(x) for x in str_time.split(':')]
    return hours * 60 * 60 + minutes * 60 + seconds


def convert_seconds_to_str_time(seconds):
    seconds %= 24 * 60 * 60
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


# Robots name - process time
robots_data = input().split(';')
robots_process_time = {}
robots_busy_time = {}

for robot in robots_data:
    name, process_time = robot.split('-')
    robots_process_time[name] = int(process_time)
    robots_busy_time[name] = -1

time = convert_str_to_seconds(input())

total_items = deque()

while True:
    command = input()
    if command == 'End':
        break
    total_items.append(command)

while total_items:
    time += 1
    item = total_items.popleft()
    for name, busy_time in robots_busy_time.items():
        if time >= busy_time:
            print(f"{name} - {item} [{convert_seconds_to_str_time(time)}]")
            robots_busy_time[name] = time + robots_process_time[name]
            break
    else:
        total_items.append(item)
