hour = int(input())
min = int(input())
total_time = (hour * 60) + min + 15
current_min = total_time % 60
current_hour = total_time // 60

if current_hour > 23:
    print(f'0:{current_min:02d}')
else:
    print(f'{current_hour}:{current_min:02d}')
