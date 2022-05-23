from math import floor

series_name = input()
seasons = int(input())
episodes = int(input())
time = float(input())
ads = time * 0.20
time_with_ads = ads + time
added_time = seasons * 10
total_time = floor(time_with_ads * episodes * seasons + added_time)
print(f'Total time needed to watch the {series_name} series is {total_time} minutes.')