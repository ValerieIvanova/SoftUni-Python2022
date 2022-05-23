min_walk_per_day = int(input())
count_of_walks_per_day = int(input())
calories_in_per_day = int(input())

total_min_per_day = min_walk_per_day * count_of_walks_per_day
total_calories_burned = total_min_per_day * 5
fifty_percent_of_cal = calories_in_per_day / 2

if total_calories_burned >= fifty_percent_of_cal:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_calories_burned}.")
elif total_calories_burned < fifty_percent_of_cal:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_calories_burned}.")
