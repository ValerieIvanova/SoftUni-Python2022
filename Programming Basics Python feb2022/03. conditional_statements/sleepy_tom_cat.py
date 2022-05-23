holiday = int(input())

holiday_play = holiday * 127
work_days = 365 - holiday
work_days_play = work_days * 63
total_play_min = work_days_play + holiday_play
difference = abs(30000 - total_play_min)
difference_in_hours = difference // 60
difference_in_min = f"{difference % 60: 02d}"


if total_play_min >= 30000:
    print('Tom will run away')
    print(f"{difference_in_hours} hours and{difference_in_min} minutes more for play")
else:
    print('Tom sleeps well')
    print(f'{difference_in_hours} hours and{difference_in_min} minutes less for play')
