hour = 23
min = 59

for i in range(hour + 1):
    for j in range(min + 1):
        if min < 60:
            print(f'{i} : {j}')