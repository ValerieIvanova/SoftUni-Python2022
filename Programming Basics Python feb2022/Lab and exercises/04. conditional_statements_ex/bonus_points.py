# points = int(input())
# bonus_points = 0
#
# if points <= 100:
#     bonus_points += 5
# elif 100 < points <= 1000:
#     bonus_points += points * 0.20
# elif points > 1000:
#     bonus_points += points * 0.10
#
# if points % 2 == 0:
#     bonus_points += 1
# elif points % 5 == 0:
#     bonus_points += 2
#
# sum_points = points + bonus_points
# print(bonus_points)
# print(sum_points)

points = int(input())
bonus_points = 0

if points <= 100:
    bonus_points += 5
elif 100 < points <= 1000:
    bonus_points += points * 0.2
else:
    bonus_points += points * 0.1

if points % 2 == 0:
    bonus_points += 1
elif points % 5 == 0:
    bonus_points += 2
sum_points = bonus_points + points
print(bonus_points)
print(sum_points)
