from math import floor

record_in_sec = float(input())
distance_in_meters = float(input())
seconds_per_meter = float(input())

seconds_for_the_whole_distance = distance_in_meters * seconds_per_meter
delay = floor(distance_in_meters / 15) * 12.5

total_time = seconds_for_the_whole_distance + delay
diff = abs(total_time - record_in_sec)

if total_time < record_in_sec:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
