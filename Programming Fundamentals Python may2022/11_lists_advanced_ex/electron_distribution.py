electrons = int(input())
shells = list()

for i in range(1, electrons + 1):
    shells.insert(i-1, 2 * i ** 2)
    if electrons - shells[i-1] <= 0:
        break
    electrons -= shells[i-1]

if electrons < shells[-1]:
    shells[-1] = electrons

print(shells)