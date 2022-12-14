from exam_prep.oop_exam_11_dec_21.project.car.muscle_car import MuscleCar
from exam_prep.oop_exam_11_dec_21.project.car.sports_car import SportsCar
from exam_prep.oop_exam_11_dec_21.project.driver import Driver
from exam_prep.oop_exam_11_dec_21.project.race import Race


class Controller:
    def __init__(self):
        self.cars = []  # all cars (objects)
        self.drivers = []  # all drivers (objects)
        self.races = []  # all races (objects)

    def __check_car_existence(self, model):
        for car in self.cars:
            if model == car.model:
                return car

    def __check_available_cars(self, car_type):
        if car_type in ['MuscleCar', 'SportsCar']:
            for i in range(len(self.cars) - 1, -1, -1):
                if car_type == self.cars[i].__class__.__name__ \
                        and not self.cars[i].is_taken:
                    return self.cars[i]

    def __check_driver_existence(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver

    def __check_race_existence(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in ['MuscleCar', 'SportsCar']:
            car = self.__check_car_existence(model)
            if car:
                raise Exception(f"Car {model} is already created!")

            if car_type == 'MuscleCar':
                new_car = MuscleCar(model, speed_limit)
            else:
                new_car = SportsCar(model, speed_limit)

            self.cars.append(new_car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver = self.__check_driver_existence(driver_name)
        if driver:
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        race = self.__check_race_existence(race_name)
        if race:
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__check_driver_existence(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        car = self.__check_available_cars(car_type)
        if not car:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car:
            old_model = driver.car.model
            driver.car.is_taken = False
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_model} to {car.model}."

        driver.car = car
        car.is_taken = True
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__check_race_existence(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        driver = self.__check_driver_existence(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__check_race_existence(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        result = []

        for driver in sorted(race.drivers, key=lambda x: x.car.speed_limit, reverse=True):
            result.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")
            driver.number_of_wins += 1
            if len(result) == 3:
                return '\n'.join(result)