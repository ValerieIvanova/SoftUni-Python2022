number_of_loads = int(input())
bus_tons = 0
truck_tons = 0
train_tons = 0
for i in range(number_of_loads):
    tons = int(input())
    if tons <= 3:
        bus_tons += tons
    elif 4 <= tons <= 11:
        truck_tons += tons
    elif tons >= 12:
        train_tons += tons
total_tons = bus_tons + truck_tons + train_tons
avr_price = ((bus_tons * 200) + (truck_tons * 175) + (train_tons * 120)) / total_tons
bus_tons_percent = bus_tons / total_tons * 100
truck_tons_percent = truck_tons / total_tons * 100
train_tons_percent = train_tons / total_tons * 100

print(f'{avr_price:.2f}')
print(f'{bus_tons_percent:.2f}%')
print(f'{truck_tons_percent:.2f}%')
print(f'{train_tons_percent:.2f}%')