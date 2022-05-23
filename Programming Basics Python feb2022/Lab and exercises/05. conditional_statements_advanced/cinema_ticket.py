day_of_week = input()
cost = 0

if day_of_week == 'Monday':
    cost = 12
elif day_of_week == 'Tuesday':
    cost = 12
elif day_of_week == 'Wednesday':
    cost = 14
elif day_of_week == 'Thursday':
    cost = 14
elif day_of_week == 'Friday':
    cost = 12
elif day_of_week == 'Saturday':
    cost = 16
elif day_of_week == 'Sunday':
    cost = 16

print(cost)