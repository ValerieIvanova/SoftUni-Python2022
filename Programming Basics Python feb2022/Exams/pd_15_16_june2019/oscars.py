actor_name = input()
points_from_academy = float(input())
number_of_judges = int(input())
total_points = points_from_academy
nominated = False
for i in range(1, number_of_judges + 1):
    judge_name = input()
    judge_points = float(input())
    total_points += (len(judge_name) * judge_points) / 2
    if total_points > 1250.5:
        nominated = True
        print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
        break
if not nominated:
    diff = abs(1250.5 - total_points)
    print(f'Sorry, {actor_name} you need {diff:.1f} more!')