# count_of_words = int(input())
# synonym_dict = {}
# for _ in range(count_of_words):
#     current_word = input()
#     synonym = input()
#     if current_word not in synonym_dict:
#         synonym_dict[current_word] = []
#     synonym_dict[current_word].append(synonym)
#
# for word, syn in synonym_dict.items():
#     print(f"{word} - {', '.join(syn)}")

from collections import defaultdict
synonyms = defaultdict(list)
count_of_words = int(input())
for _ in range(count_of_words):
    word, synonym = input(), input()
    synonyms[word].append(synonym)
data = [f"{word} - {', '.join(synonym)}" for word, synonym in synonyms.items()]
print('\n'.join(data))