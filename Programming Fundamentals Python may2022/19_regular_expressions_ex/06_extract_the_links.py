import re

pattern = r'((w{3}\.)([\-?A-Za-z0-9]+)(\.[a-z]+)(\.[a-z]+)*)'
links = []
while True:
    string = input()
    if string == '':
        break
    matches = re.search(pattern, string)
    if matches:
        link = matches.group()
        links.append(link)
[print(link) for link in links]