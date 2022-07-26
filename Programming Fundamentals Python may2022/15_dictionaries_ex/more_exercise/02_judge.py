def adding_contests(username_, contest_, points_):
    if contest_ not in judge_dict:
        judge_dict[contest_] = {}
    if username_ not in judge_dict[contest_]:
        judge_dict[contest_] = judge_dict.get(contest_, {})
        judge_dict[contest_][username_] = 0
    if int(points_) > judge_dict[contest_][username_]:
        judge_dict[contest_][username_] = int(points_)
    return judge_dict


def get_total_points(general_dict, points_dict):
    for course_, users_ in general_dict.items():
        for user_ in users_:
            if user_ not in points_dict:
                points_dict[user_] = 0
            points_dict[user_] += general_dict[course_][user_]
    return points_dict


judge_dict = {}

while True:
    command = input()
    if command == 'no more time':
        break
    username, contest, points = command.split(' -> ')
    adding_contests(username, contest, points)

# Print courses data:
for course, users in judge_dict.items():
    print(f"{course}: {len(users)} participants")
    n = 1
# Print participants' data sorted by points in descending order, then ascending name order:
    for person, points in sorted(users.items(), key=lambda x: (-x[1], x[0])):
        print(f"{n}. {person} <::> {points}")
        n += 1
print("Individual standings:")
# Get the total points for every participant and store them in a new dict:
total_points = {}
get_total_points(judge_dict, total_points)
# Print individual statistics for every participant ordered by total points in descending order,
# then alphabetical order:
n = 1
for user, points in sorted(total_points.items(), key=lambda x: (-x[1], x[0])):
    print(f"{n}. {user} -> {points}")
    n += 1