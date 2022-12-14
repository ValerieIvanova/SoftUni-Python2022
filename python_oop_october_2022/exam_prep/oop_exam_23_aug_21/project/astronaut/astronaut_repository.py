from exam_prep.oop_exam_23_aug_21.project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        if astronaut not in self.astronauts:
            self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        if astronaut in self.astronauts:
            self.astronauts.remove(astronaut)

    def find_by_name(self, name):
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut

    def details(self):
        result = []
        for a in self.astronauts:
            result.append(f"Name: {a.name}\n"
                          f"Oxygen: {a.oxygen}\n"
                          f"Backpack items: {', '.join(a.backpack) if a.backpack else 'none'}")
        return '\n'.join(result)
