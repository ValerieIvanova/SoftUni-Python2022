import sys
from math import floor

current_sum = 0
max_sum = -sys.maxsize
vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
most_powerful_word = ''
while True:
    word = input()
    if word == 'End of words':
        break
    for i in range(len(word)):         #for ch in word
        current_sum += ord(word[i])
    if word[0] in vowels:
        current_sum = current_sum * len(word)
    else:
        current_sum = floor(current_sum / len(word))
    if current_sum >= max_sum:
        max_sum = current_sum
        most_powerful_word = word
    current_sum = 0
print(f'The most powerful word is {most_powerful_word} - {max_sum}')