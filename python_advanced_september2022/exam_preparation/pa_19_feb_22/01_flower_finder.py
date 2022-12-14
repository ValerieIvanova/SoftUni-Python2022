from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())
WORDS = ['rose', 'tulip', 'lotus', 'daffodil']
searched_words = ['rose', 'tulip', 'lotus', 'daffodil']
word_found = False
while True:
    if not vowels or not consonants:
        break
    vowel, consonant = vowels.popleft(), consonants.pop()
    for i in range(len(searched_words)):
        if vowel in searched_words[i] or consonant in searched_words[i]:
            searched_words[i] = searched_words[i].replace(vowel, '')
            searched_words[i] = searched_words[i].replace(consonant, '')
            if searched_words[i] == '':
                word_found = True
                break
    if word_found:
        break

if not word_found:
    print("Cannot find any word!")
else:
    found_word_idx = searched_words.index('')
    print(f"Word found: {WORDS[found_word_idx]}")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")