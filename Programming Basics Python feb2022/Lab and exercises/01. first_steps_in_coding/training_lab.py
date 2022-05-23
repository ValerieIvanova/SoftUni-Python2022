w = float(input())
h = float(input())

# hallway = 100cm
# desk width = 120
# desk height = 70
width = (h * 100) - 100
desks_in_a_row_h = int(width / 70)

hight = w * 100
rows_w = int(hight / 120)

total_desks = rows_w * desks_in_a_row_h - 3

print(total_desks)