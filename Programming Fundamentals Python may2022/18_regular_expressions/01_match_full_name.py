import re
characters = input()
pattern = r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b"
print(*(re.findall(pattern, characters)))