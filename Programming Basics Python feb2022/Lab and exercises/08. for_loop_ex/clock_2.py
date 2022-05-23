hour = 23
min = 59
sec = 59

for h in range(hour + 1):
    for m in range(min + 1):
        if min < 60:
            for s in range(sec + 1):
                if sec < 60:
                    print(f'{h} : {m} : {s}')