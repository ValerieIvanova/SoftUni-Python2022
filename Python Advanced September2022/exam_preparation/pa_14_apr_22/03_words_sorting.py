def words_sorting(*args):
    words_dict = {}
    sum_values = 0

    for word in args:
        if word not in words_dict:
            words_dict[word] = 0
        words_dict[word] += sum([ord(el) for el in word])
        sum_values += words_dict[word]

    result = []

    if sum_values % 2 != 0:
        sorted_words = sorted(words_dict.items(), key=lambda x: -x[1])
    else:
        sorted_words = sorted(words_dict.items(), key=lambda x: x[0])

    for key, value in sorted_words:
        result.append(f"{key} - {value}")

    return '\n'.join(result)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
