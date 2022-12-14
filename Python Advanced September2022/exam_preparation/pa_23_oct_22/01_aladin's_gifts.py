from collections import deque


def check_present(present_, presents_dict):
    if 100 <= present_ <= 199:
        presents_dict["Gemstone"] += 1
    elif 200 <= present_ <= 299:
        presents_dict["Porcelain Sculpture"] += 1
    elif 300 <= present_ <= 399:
        presents_dict["Gold"] += 1
    elif 400 <= present_ <= 499:
        presents_dict["Diamond Jewellery"] += 1
    return presents_dict


def output():
    result = ''
    if all([presents["Gemstone"], presents["Porcelain Sculpture"]]) or all(
            [presents["Gold"], presents["Diamond Jewellery"]]):
        result += "The wedding presents are made!\n"
    else:
        result += "Aladdin does not have enough wedding presents.\n"

    if materials:
        result += f"Materials left: {', '.join(map(str, materials))}\n"

    if magic:
        result += f"Magic left: {', '.join(map(str, magic))}\n"

    for gift, val in sorted(presents.items()):
        if val:
            result += f"{gift}: {val}\n"

    return result


materials = deque([int(x) for x in input().split()])
magic = deque([int(x) for x in input().split()])
presents = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

while materials and magic:
    current_material = materials.pop()
    current_magic_lvl = magic.popleft()
    present = current_material + current_magic_lvl

    if present < 100:
        if present % 2 == 0:
            present = current_material * 2 + current_magic_lvl * 3
        else:
            present *= 2

    elif present > 499:
        present /= 2

    presents = check_present(present, presents)

print(output())