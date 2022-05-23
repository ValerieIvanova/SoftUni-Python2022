hour_of_the_exam = int(input())
min_of_the_exam = int(input())
hour_of_arrival = int(input())
min_of_arrival = int(input())

total_min_of_the_exam = hour_of_the_exam * 60 + min_of_the_exam
total_min_of_arrival = hour_of_arrival * 60 + min_of_arrival
diff = abs(total_min_of_the_exam - total_min_of_arrival)

if total_min_of_the_exam == total_min_of_arrival:
    print('On time')
elif total_min_of_arrival < total_min_of_the_exam:
    if diff <= 30:
        print('On time')
        print(f'{diff} minutes before the start')
    else:
        print('Early')
        hour = diff // 60
        min = diff % 60
        if diff > 59:
            print(f'{hour}:{min:02d} hours before the start')
        else:
            print(f'{min} minutes before the start')
elif total_min_of_arrival > total_min_of_the_exam:
    print('Late')
    hour = diff // 60
    min = diff % 60
    if diff > 59:
        print(f'{hour}:{min:02d} hours after the start')
    else:
        print(f'{min} minutes after the start')