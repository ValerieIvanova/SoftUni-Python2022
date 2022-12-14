from exam_prep.oop_exam_23_aug_21.project.planet.planet import Planet


class PlanetRepository:
    def __init__(self):
        self.planets = []  # an empty list of planets

    def add(self, planet: Planet):
        if planet not in self.planets:
            self.planets.append(planet)

    def remove(self, planet: Planet):
        if planet in self.planets:
            self.planets.remove(planet)

    def find_by_name(self, name):
        for planet in self.planets:
            if planet.name == name:
                return planet