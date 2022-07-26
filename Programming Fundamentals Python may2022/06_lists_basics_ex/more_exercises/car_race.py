numbers = input().split()
finish_line = len(numbers) // 2
left_car = numbers[:finish_line]
right_car = numbers[finish_line+1:]
left = 0
right = 0
for time_first_racer in range(len(left_car)):
    left += int(left_car[time_first_racer])
    if int(left_car[time_first_racer]) == 0:
        left -= left * 0.2

for time_second_racer in range(len(right_car) - 1, -1, -1):
    right += int(right_car[time_second_racer])
    if int(right_car[time_second_racer]) == 0:
        right -= right * 0.2
if min(left, right) == left:
    racer = 'left'
else:
    racer = 'right'
print(f'The winner is {racer} with total time: {min(left, right):.1f}')