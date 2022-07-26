days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
gathered = 0

for day in range(1, days + 1):
    gathered += daily_plunder
    if day % 3 == 0:
        gathered += daily_plunder / 2
    if day % 5 == 0:
        gathered -= gathered * 0.3

if gathered >= expected_plunder:
    print(f"Ahoy! {gathered:.2f} plunder gained.")
else:
    percentage = (100 / expected_plunder) * gathered
    print(f'Collected only {percentage:.2f}% of the plunder.')
