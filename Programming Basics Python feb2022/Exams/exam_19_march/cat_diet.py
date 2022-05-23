percent_fats = int(input())
percent_protein = int(input())
percent_carbohydrates = int(input())
total_calories = int(input())
percent_water = int(input())

total_grams_fat = (total_calories * (percent_fats / 100)) / 9
total_grams_protein = (total_calories * (percent_protein / 100)) / 4
total_grams_carbohydrates = (total_calories * (percent_carbohydrates / 100)) / 4
total_grams = total_grams_protein + total_grams_carbohydrates + total_grams_fat
calories_per_gram = total_calories / total_grams
calories_without_water = calories_per_gram - (calories_per_gram * (percent_water / 100))
print(f"{calories_without_water:.4f}")