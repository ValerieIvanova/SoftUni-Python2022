total_steps = 0
while True:
    number_of_steps = input()
    if number_of_steps == 'Going home':
        additional_steps = int(input())
        total_steps += additional_steps
        diff = abs(10000 - total_steps)
        if total_steps < 10000:
            print(f'{diff} more steps to reach goal.')
        if total_steps >= 10000:
            print(f'Goal reached! Good job!')
            print(f'{diff} steps over the goal!')
        break
    total_steps += int(number_of_steps)
    if total_steps >= 10000:
        diff = abs(10000 - total_steps)
        print(f'Goal reached! Good job!')
        print(f'{diff} steps over the goal!')
        break