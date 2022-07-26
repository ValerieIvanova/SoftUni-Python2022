from math import floor

biscuits_per_day_worker = int(input())
workers = int(input())
competing_factory_monthly_production = int(input())

daily_production = workers * biscuits_per_day_worker
total_production = 0
for day in range(1, 30 + 1):
    if day % 3 == 0:
        total_production += floor(daily_production * 0.75)
    else:
        total_production += daily_production

diff = abs(total_production - competing_factory_monthly_production)
percentage = (diff / competing_factory_monthly_production) * 100

print(f"You have produced {total_production} biscuits for the past month.")

if total_production > competing_factory_monthly_production:
    print(f"You produce {percentage:.2f} percent more biscuits.")
elif total_production < competing_factory_monthly_production:
    print(f"You produce {percentage:.2f} percent less biscuits.")