capacity = float(input())
loads = 0
while True:
    suitcase_size = input()
    if suitcase_size == 'End':
        print("Congratulations! All suitcases are loaded!")
        break
    suitcase_size = float(suitcase_size)
    loads += 1
    if loads % 3 == 0:
        suitcase_size += suitcase_size * 0.10
    if suitcase_size > capacity:
        loads -= 1
        print("No more space!")
        break
    capacity -= suitcase_size
print(f"Statistic: {loads} suitcases loaded.")