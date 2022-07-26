import re

sentence = input()
word = input()
pattern = fr"\b{word}\b"
matches = re.findall(pattern, sentence, flags=re.IGNORECASE)
print(len(matches))