v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

total_liters_p1 = p1 * h
total_liters_p2 = p2 * h
total_liters = total_liters_p1 + total_liters_p2

p1_liters_in_percent = total_liters_p1 / total_liters * 100
p2_liters_in_percent = total_liters_p2 / total_liters * 100
total_liters_in_percent = total_liters / v * 100
diff = abs(v - total_liters)
if total_liters <= v:
    print(f"The pool is {total_liters_in_percent:.2f}% full. Pipe 1: {p1_liters_in_percent:.2f}%. "
          f"Pipe 2: {p2_liters_in_percent:.2f}%.")
else:
    print(f"For {h} hours the pool overflows with {diff} liters.")
