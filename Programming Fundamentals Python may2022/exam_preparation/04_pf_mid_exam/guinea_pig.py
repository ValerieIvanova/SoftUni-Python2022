food = float(input())
hay = float(input())
cover = float(input())
weight = float(input())
food_in_grams = food * 1000
hay_in_grams = hay * 1000
cover_in_grams = cover * 1000
weight_in_grams = weight * 1000
enough_food = True
enough_hay = True
enough_cover = True
for day in range(1, 31):
    if 0 < food_in_grams - 300 < food_in_grams:
        food_in_grams -= 300
        if day % 2 == 0:
            if 0 < hay_in_grams - food_in_grams * 0.05 < hay_in_grams:
                hay_in_grams -= food_in_grams * 0.05
            else:
                enough_hay = False
                break
        if day % 3 == 0:
            if 0 < cover_in_grams - weight_in_grams / 3 < cover_in_grams:
                cover_in_grams -= weight_in_grams / 3
            else:
                enough_cover = False
                break
    else:
        enough_food = False
        break
if enough_food and enough_hay and enough_cover:
    print(f'Everything is fine! Puppy is happy! Food: {food_in_grams/1000:.2f}, Hay: {hay_in_grams/1000:.2f}, '
          f'Cover: {cover_in_grams/1000:.2f}.')
else:
    print('Merry must go to the pet store!')