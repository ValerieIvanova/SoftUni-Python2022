submissions_dict = {}
banned_user = ''
submissions_count = {}
while True:
    command = input()
    if command == 'exam finished':
        break
    command.split('-')
    if 'banned' in command:
        username = command.split('-')[0]
        for language in submissions_dict:
            for member in submissions_dict[language]:
                if username == member:
                    banned_user = username
                    break
        continue
    username, language, points = command.split('-')
    if language not in submissions_dict:
        submissions_dict[language] = {}
        submissions_count[language] = 0
    if username not in submissions_dict[language]:
        submissions_dict[language][username] = []
    submissions_dict[language][username].append(int(points))
    submissions_count[language] += 1

print("Results:")
for language in submissions_dict:
    for participant in submissions_dict[language]:
        if participant != banned_user:
            print(f"{participant} | {max(submissions_dict[language][participant])}")
print("Submissions:")
[print(f"{language} - {submissions_count[language]}") for language, person in submissions_dict.items()]
