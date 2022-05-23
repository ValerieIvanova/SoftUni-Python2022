stadium_capacity = int(input())
number_of_fans = int(input())
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for i in range(number_of_fans):
    sector = input()
    if sector == 'A':
        sector_a += 1
    elif sector == 'B':
        sector_b += 1
    elif sector == 'V':
        sector_v += 1
    elif sector == 'G':
        sector_g += 1

sector_a_percent = sector_a / number_of_fans * 100
sector_b_percent = sector_b / number_of_fans * 100
sector_v_percent = sector_v / number_of_fans * 100
sector_g_percent = sector_g / number_of_fans * 100
total_fans_percent = number_of_fans / stadium_capacity * 100

print(f'{sector_a_percent:.2f}%')
print(f'{sector_b_percent:.2f}%')
print(f'{sector_v_percent:.2f}%')
print(f'{sector_g_percent:.2f}%')
print(f'{total_fans_percent:.2f}%')