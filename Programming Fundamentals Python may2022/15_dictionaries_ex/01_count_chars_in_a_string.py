# 1:
# from collections import defaultdict
#
# current_string = input()
# occurrences = defaultdict(int)
# for let in current_string:
#     if let != ' ':
#         occurrences[let] += 1
# for key, value in occurrences.items():
#     print(f"{key} -> {value}")

# 2--------------------------------------------------:

from collections import Counter

word = ''.join(s for s in input().split())
result = Counter(word)
[print(f"{char} -> {count}") for char, count in result.items()]

# 3--------------------------------------------------:

# characters = input()
# counter = {}
# for char in characters:
#     if char != ' ':
#         if char not in counter:
#             counter[char] = 1
#         else:
#             counter[char] += 1
#
# [print(f"{char} -> {count}") for char, count in counter.items()]