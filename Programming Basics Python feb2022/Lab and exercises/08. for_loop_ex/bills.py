months = int(input())
total_electricity_bill = 0
total_water_bill = 0
total_internet_bill = 0
total_other_bills = 0

for i in range(months):
    electricity_bill = float(input())
    total_electricity_bill += electricity_bill
    total_water_bill += 20
    total_internet_bill += 15
    total_other_bills += (electricity_bill + 20 + 15) + (electricity_bill + 20 + 15) * 0.2

total_bills = total_electricity_bill + total_water_bill + total_internet_bill + total_other_bills
avr_bills = total_bills / months

print(f'Electricity: {total_electricity_bill:.2f} lv')
print(f'Water: {total_water_bill:.2f} lv')
print(f'Internet: {total_internet_bill:.2f} lv')
print(f'Other: {total_other_bills:.2f} lv')
print(f'Average: {avr_bills:.2f} lv')