import math

hours_needed = int(input())
days = int(input())
overtime_workers = int(input())

days_available = days - days * 0.10
working_hours = days_available * 8
overtime_worker_hours = overtime_workers * (2 * days)
total_hours = math.floor(working_hours + overtime_worker_hours)
diff = abs(total_hours - hours_needed)

if total_hours >= hours_needed:
    print(f"Yes!{diff} hours left.")
else:
    print(f"Not enough time!{diff} hours needed.")