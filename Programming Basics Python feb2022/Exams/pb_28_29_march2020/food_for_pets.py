days = int(input())
food_quantity = float(input())
biscuits = 0
total_dog_food = 0
total_cat_food = 0
for i in range(1, days + 1):
    dog_food_quantity = int(input())
    total_dog_food += dog_food_quantity
    cat_food_quantity = int(input())
    total_cat_food += cat_food_quantity
    if i % 3 == 0:
        biscuits += (dog_food_quantity + cat_food_quantity) * 0.10
total_food = total_dog_food + total_cat_food
percent_total_food = (total_food / food_quantity) * 100
percent_dog_food = (total_dog_food / total_food) * 100
percent_cat_food = (total_cat_food / total_food) * 100
print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{percent_total_food:.2f}% of the food has been eaten.")
print(f"{percent_dog_food:.2f}% eaten from the dog.")
print(f"{percent_cat_food:.2f}% eaten from the cat.")
