total_food_kg = int(input())
total_food_gr = total_food_kg * 1000
food_eaten = 0
while True:
    food_gr = input()
    if food_gr == 'Adopted':
        break
    food_eaten += int(food_gr)
diff = abs(total_food_gr - food_eaten)
if food_eaten <= total_food_gr:
    print(f'Food is enough! Leftovers: {diff} grams.')
else:
    print(f'Food is not enough. You need {diff} grams more.')