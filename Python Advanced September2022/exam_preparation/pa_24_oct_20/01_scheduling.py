jobs = [int(x) for x in input().split(', ')]
searched_idx = int(input())

clock_cycles = 0
i = 0

while True:
    task = min(jobs)
    i = jobs.index(task)
    clock_cycles += task
    if i == searched_idx:
        break
    jobs[i] = 999999

print(clock_cycles)
