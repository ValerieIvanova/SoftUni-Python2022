number_of_snowballs = int(input())
max_value = 0
winner_weight = 0
winner_time = 0
winner_quality = 0

for i in range(number_of_snowballs):
    weight = int(input())
    needed_time = int(input())
    quality = int(input())
    value = (weight / needed_time) ** quality
    if value > max_value:
        max_value = value
        winner_weight = weight
        winner_time = needed_time
        winner_quality = quality

print(f'{winner_weight} : {winner_time} = {int(max_value)} ({winner_quality})')