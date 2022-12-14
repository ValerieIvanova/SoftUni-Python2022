def naughty_or_nice_list(santa_list, *args, **kwargs):
    naughty_kids = []
    nice_kids = []
    not_found = []

    for data in args:
        d = data.split('-')
        counting_number = int(d[0])
        command = d[1]

        count = 0
        idx = 0
        for i, info in enumerate(santa_list):
            if counting_number in info:
                count += 1
                idx = i
                if count > 1:
                    break
        if count == 1:
            if command == 'Naughty':
                naughty_kids.append(santa_list.pop(idx)[1])
            elif command == 'Nice':
                nice_kids.append(santa_list.pop(idx)[1])

    if kwargs:
        for name, val in kwargs.items():
            count = 0
            idx = 0
            for i, info in enumerate(santa_list):
                if name in info:
                    count += 1
                    idx = i
                    if count > 1:
                        break
            if count == 1:
                if val == 'Naughty':
                    naughty_kids.append(santa_list.pop(idx)[1])
                elif val == 'Nice':
                    nice_kids.append(santa_list.pop(idx)[1])

    if santa_list:
        for data in santa_list:
            not_found.append(data[1])

    result = ''
    if nice_kids:
        result += f"Nice: {', '.join(nice_kids)}"
    if naughty_kids:
        result += f"\nNaughty: {', '.join(naughty_kids)}"
    if not_found:
        result += f"\nNot found: {', '.join(not_found)}"
    return result


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))


print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
