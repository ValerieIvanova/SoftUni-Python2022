import re

text = input()
emojis_pattern = r"((::|\*\*)([A-Z][a-z]{2,})\2)"
threshold_pattern = r"\d"
emojis = re.findall(emojis_pattern, text)
cool_threshold_digits = re.findall(threshold_pattern, text)
cool_threshold = 1
for digit in cool_threshold_digits:
    cool_threshold *= int(digit)

print(f'Cool threshold: {cool_threshold}')
print(f'{len(emojis)} emojis found in the text. The cool ones are:')
for item in emojis:
    current_coolness = 0
    for char in item[2]:
        current_coolness += ord(char)
    if current_coolness >= cool_threshold:
        print(item[0])