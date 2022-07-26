level_of_fire = input().split('#')
water_amount = int(input())
total_effort = 0
total_fire = 0
put_out_cells = []
for element in level_of_fire:
    fire_info = element.split(' = ')
    type_of_fire = fire_info[0]
    cell_value = int(fire_info[1])
    valid = False
    if cell_value > water_amount:
        continue
    if type_of_fire == 'High':
        if 81 <= cell_value <= 125:
            valid = True
    elif type_of_fire == 'Medium':
        if 51 <= cell_value <= 80:
            valid = True
    elif type_of_fire == 'Low':
        if 1 <= cell_value <= 50:
            valid = True
    if valid:
        water_amount -= cell_value
        total_effort += cell_value * 0.25
        total_fire += cell_value
        put_out_cells.append(cell_value)
print(f'Cells:')
for cell in put_out_cells:
    print(f' - {cell}')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')