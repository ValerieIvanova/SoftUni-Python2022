import re

dates = input()
pattern = r"\b(?P<day>\d{2})(?P<sep>[/\-.])(?P<month>[A-Z][a-z]{2})(?P=sep)(?P<year>\d{4})\b"
valid_dates = re.finditer(pattern, dates)
for info in valid_dates:
    print(f"Day: {info.group('day')}, Month: {info.group('month')}, Year: {info.group('year')}")