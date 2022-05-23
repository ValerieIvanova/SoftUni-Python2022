km = int(input())
time = input()

bus = km * 0.09
train = km * 0.06
taxi = 0

if time == "day":
    taxi = 0.70 + km * 0.79
elif time == "night":
    taxi = 0.70 + km * 0.90

if km < 20:
    print(f"{taxi:.2f}")
elif 20 <= km < 100:
    print(f'{bus:.2f}')
elif 100 <= km:
    print(f'{train:.2f}')
