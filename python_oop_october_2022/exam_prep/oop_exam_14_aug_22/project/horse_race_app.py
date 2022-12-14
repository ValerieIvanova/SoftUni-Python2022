from exam_prep.oop_exam_14_aug_22.project.horse_race import HorseRace
from exam_prep.oop_exam_14_aug_22.project.horse_specification.appaloosa import Appaloosa
from exam_prep.oop_exam_14_aug_22.project.horse_specification.thoroughbred import Thoroughbred
from exam_prep.oop_exam_14_aug_22.project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_TYPES_REF = {'Appaloosa': Appaloosa,
                             'Thoroughbred': Thoroughbred
                             }

    def __init__(self):
        self.horses = []  # all the horses (objects)
        self.jockeys = []  # all the jockeys (objects)
        self.horse_races = []  # all the horse races (objects)

    def __check_horse(self, horse_type):
        for horse in reversed(self.horses):
            if not horse.is_taken and horse.__class__.__name__ == horse_type:
                return horse
        raise Exception(f"Horse breed {horse_type} could not be found!")

    def __check_jockey(self, jockey_name):
        for jockey in self.jockeys:
            if jockey_name == jockey.name:
                return jockey
        raise Exception(f"Jockey {jockey_name} could not be found!")

    def __check_race(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race
        raise Exception(f"Race {race_type} could not be found!")

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_name in [h.name for h in self.horses]:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.VALID_HORSE_TYPES_REF:
            self.horses.append(self.VALID_HORSE_TYPES_REF[horse_type](horse_name, horse_speed))
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if jockey_name in [j.name for j in self.jockeys]:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in [r.race_type for r in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")

        new_horse_race = HorseRace(race_type)
        self.horse_races.append(new_horse_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__check_jockey(jockey_name)
        horse = self.__check_horse(horse_type)
        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.__check_race(race_type)
        jockey = self.__check_jockey(jockey_name)

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.__check_race(race_type)
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        highest_speed = 0
        jockey_name = ''
        horse_name = ''
        for jokey in race.jockeys:
            if jokey.horse.speed > highest_speed:
                highest_speed = jokey.horse.speed
                jockey_name = jokey.name
                horse_name = jokey.horse.name

        return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is " \
               f"{jockey_name}! Winner's horse: {horse_name}."

# horseRaceApp = HorseRaceApp()
# print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
# print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))
# print(horseRaceApp.add_horse("aa", "aa", 110))
# print(horseRaceApp.add_jockey("Peter", 19))
# print(horseRaceApp.add_jockey("Mariya", 21))
# print(horseRaceApp.create_horse_race("Summer"))
# print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
# print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
# print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
# print(horseRaceApp.start_horse_race("Summer"))
