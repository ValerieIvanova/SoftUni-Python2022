from exam_prep.oop_exam_23_aug_21.project.astronaut.astronaut_repository import AstronautRepository
from exam_prep.oop_exam_23_aug_21.project.astronaut.biologist import Biologist
from exam_prep.oop_exam_23_aug_21.project.astronaut.geodesist import Geodesist
from exam_prep.oop_exam_23_aug_21.project.astronaut.meteorologist import Meteorologist
from exam_prep.oop_exam_23_aug_21.project.planet.planet import Planet
from exam_prep.oop_exam_23_aug_21.project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.not_completed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in ["Biologist", "Geodesist", "Meteorologist"]:
            raise Exception("Astronaut type is not valid!")

        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut:
            return f"{name} is already added."

        if astronaut_type == 'Biologist':
            new_astronaut = Biologist(name)
        elif astronaut_type == 'Geodesist':
            new_astronaut = Geodesist(name)
        else:
            new_astronaut = Meteorologist(name)

        self.astronaut_repository.add(new_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        planet = self.planet_repository.find_by_name(name)
        if planet:
            return f"{name} is already added."

        new_planet = Planet(name)
        new_planet.items.extend(items.split(', '))
        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.increase_oxygen(10)

    def send_on_mission(self, planet_name):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")

        astronauts = [a for a in self.astronaut_repository.astronauts if a.oxygen > 30]

        if not astronauts:
            self.not_completed_missions += 1
            raise Exception("You need at least one astronaut to explore the planet!")

        number_of_astronauts = 1
        for astronaut in sorted(astronauts, key=lambda x: -x.oxygen)[:5]:
            while 'none' in astronaut.backpack:
                astronaut.backpack.remove('none')
            for i in range(len(planet.items)):
                if astronaut.oxygen <= 0:
                    astronaut.oxygen = 0
                    number_of_astronauts += 1
                    break
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()

        if not planet.items:
            self.successful_missions += 1
            return f"Planet: {planet_name} was explored. {number_of_astronauts} astronauts participated in collecting items."

        self.not_completed_missions += 1
        return "Mission is not completed."

    def report(self):
        result = [f"{self.successful_missions} successful missions!",
                  f"{self.not_completed_missions} missions were not completed!", "Astronauts' info:",
                  self.astronaut_repository.details()]

        return '\n'.join(result)

#
# planet = Planet('pluto')
#
# s = SpaceStation()
# s.add_planet('pluto', 'a, d, v')
# s.add_astronaut('Biologist', 'a')
# s.add_astronaut('Biologist', 'b')
# s.add_astronaut('Biologist', 'v')
# s.add_astronaut('Biologist', 'c')
# s.add_astronaut('Biologist', 'f')
# s.send_on_mission('pluto')
# astr = Biologist('joe')
# s.recharge_oxygen()
#
# print(s.report())
