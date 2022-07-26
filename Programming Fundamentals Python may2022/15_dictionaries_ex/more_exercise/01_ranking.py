passwords_dict = {}
while True:
    command = input()
    if command == 'end of contests':
        break
    contest, password = command.split(':')
    passwords_dict[contest] = password

submissions_dict = {}
while True:
    command = input()
    if command == 'end of submissions':
        break
    contest, password, username, points = command.split('=>')
    if contest in passwords_dict and password in passwords_dict[contest]:
        submissions_dict[username] = submissions_dict.get(username, {})
        submissions_dict[username][contest] = submissions_dict[username].get(contest, 0)
        if submissions_dict[username][contest] < int(points):
            submissions_dict[username][contest] = int(points)
max_points = 0
best_user = ''
for user in submissions_dict:
    total_points = sum(submissions_dict[user].values())
    if total_points > max_points:
        max_points = total_points
        best_user = user
print(f"Best candidate is {best_user} with total {max_points} points.")
print('Ranking:')

for user in sorted(submissions_dict):
    print(user)
    for course, points in sorted(submissions_dict[user].items(), key=lambda x: -x[1]):
        print(f"#  {course} -> {points}")