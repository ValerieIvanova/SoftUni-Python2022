import re
pattern = r'\d+'

line = input()
while True:
    if line:
        match = re.findall(pattern, line)
        if match:
            print(*match, end=' ')
        line = input()
    else:
        break