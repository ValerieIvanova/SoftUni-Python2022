from math import ceil

days = int(input())
km_first_day = float(input())
norm = km_first_day
total_km = km_first_day
for d in range(1, days + 1):
    percent_increase = int(input())
    norm += norm * (percent_increase / 100)
    total_km += norm
diff = abs(total_km - 1000)
if total_km >= 1000:
    print(f"You've done a great job running {ceil(diff)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(diff)} more kilometers")