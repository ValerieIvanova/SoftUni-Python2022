import re

numbers = input()
pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
valid = re.finditer(pattern, numbers)
[print(match.group(), end=' ') for match in valid]