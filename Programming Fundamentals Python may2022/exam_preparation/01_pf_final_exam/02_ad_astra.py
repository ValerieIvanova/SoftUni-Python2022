import re

food_info = input()
pattern = r'(?P<sep>[#|])(?P<food>[A-Z][a-z]+(\s[A-Z][a-z]+)?)(?P=sep)' \
          r'(?P<date>(\d{2}/\d{2}/\d{2}))(?P=sep)(?P<cal>\d+)(?P=sep)'
# 2000 kcal per day needed
# matches = re.finditer(pattern, food_info)
# if matches:
#     calories = [int(cal.group('cal')) for cal in matches]
#     print(f"You have food to last you for: {sum(calories) // 2000} days!")
# matches = re.finditer(pattern, food_info)
# if matches:
#     for match in matches:
#         print(f"Item: {match.group('food')}, Best before: {match.group('date')}, Nutrition: {match.group('cal')}")

matches = re.findall(pattern, food_info)

calories = [int(cal[5]) for cal in matches if cal[5]]
print(f"You have food to last you for: {sum(calories)//2000} days!")
for match in matches:
    if match:
        print(f"Item: {match[1]}, Best before: {match[3]}, Nutrition: {match[5]}")