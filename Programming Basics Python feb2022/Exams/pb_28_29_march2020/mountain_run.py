import math

record_in_sec = float(input())
distance_in_meters = float(input())
sec_per_meter = float(input())

total_sec = distance_in_meters * sec_per_meter
delay = math.floor(distance_in_meters / 50) * 30
total_time = total_sec + delay
diff = abs(record_in_sec - total_time)

if total_time < record_in_sec:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {diff:.2f} seconds slower.")
