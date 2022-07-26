import re
numbers = input()
# Using positive lookbehind to see if the string starts with white space, or the row starts with +359
pattern = r"(^|(?<=\s))\+359(?P<sep>[\s-])2(?P=sep)\d{3}(?P=sep)\d{4}\b"
matches = re.finditer(pattern, numbers)
valid = [match.group() for match in matches]
print(*valid, sep=', ')