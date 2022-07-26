def add_cars(info, cars):
    car_model = info[0]
    mileage = int(info[1])
    fuel = int(info[2])
    if car_model not in cars:
        cars[car_model] = {}
    cars[car_model]['mileage'] = mileage
    cars[car_model]['fuel'] = fuel
    return cars


def drive(cars):
    car = command[1]
    distance = int(command[2])
    fuel = int(command[3])
    if fuel > cars[car]['fuel']:
        print("Not enough fuel to make that ride")
    else:
        cars[car]['mileage'] += distance
        cars[car]['fuel'] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car]['mileage'] >= 100000:
            del cars[car]
            print(f"Time to sell the {car}!")
    return cars


def refuel(cars):
    car = command[1]
    fuel = int(command[2])
    if cars[car]['fuel'] + fuel <= 75:
        cars[car]['fuel'] += fuel
        print(f"{car} refueled with {fuel} liters")
        return cars
    fuel_needed = 75 - cars[car]['fuel']
    cars[car]['fuel'] += fuel_needed
    print(f"{car} refueled with {fuel_needed} liters")
    return cars


def revert(cars):
    car = command[1]
    kilometers = int(command[2])
    cars[car]['mileage'] -= kilometers
    if cars[car]['mileage'] < 10000:
        cars[car]['mileage'] = 10000
    else:
        print(f"{car} mileage decreased by {kilometers} kilometers")
    return cars


number_of_cars = int(input())
cars_inventory = {}
for car in range(number_of_cars):
    car_info = input().split('|')
    cars_inventory = add_cars(car_info, cars_inventory)

while True:
    command = input().split(" : ")
    command_name = command[0]
    if command_name == 'Stop':
        break

    elif command_name == 'Drive':
        cars_inventory = drive(cars_inventory)

    elif command_name == 'Refuel':
        cars_inventory = refuel(cars_inventory)

    elif command_name == 'Revert':
        cars_inventory = revert(cars_inventory)

for car, info in cars_inventory.items():
    print(f"{car} -> Mileage: {info['mileage']} kms, Fuel in the tank: {info['fuel']} lt.")