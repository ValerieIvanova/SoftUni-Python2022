time_of_day = int(input())
day_of_week = input()

if 10 <= time_of_day <= 18:
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week =='Wednesday'	or day_of_week == 'Thursday' \
            or day_of_week == 'Friday' or day_of_week == 'Saturday':
        print('open')
    elif day_of_week == 'Sunday':
        print('closed')
else:
    print('closed')