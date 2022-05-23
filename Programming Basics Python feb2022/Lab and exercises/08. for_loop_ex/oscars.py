name_of_the_actor = input()
points_from_academy = float(input())
number_of_judges = int(input())

judge_total_points = 0
total_points = 0

for _ in range(number_of_judges):
    name_of_the_judge = input()
    points_from_the_judge = float(input())
    judge_total_points += (len(name_of_the_judge) * points_from_the_judge) / 2
    total_points = points_from_academy + judge_total_points
    if total_points > 1250.5:
        print(f'Congratulations, {name_of_the_actor} got a nominee for leading role with {total_points:.1f}!')
        break
if total_points <= 1250.5:
    diff = abs(total_points - 1250.5)
    print(f'Sorry, {name_of_the_actor} you need {diff:.1f} more!')