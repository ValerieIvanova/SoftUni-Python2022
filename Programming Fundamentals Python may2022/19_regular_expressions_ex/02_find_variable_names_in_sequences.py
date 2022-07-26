import re

strings = input()
pattern = r"\b_([A-Za-z0-9]+)\b"

matches = re.findall(pattern, strings)
print(*matches, sep=',')