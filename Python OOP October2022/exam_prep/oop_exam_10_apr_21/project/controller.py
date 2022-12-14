from exam_prep.oop_exam_10_apr_21.project.aquarium.freshwater_aquarium import FreshwaterAquarium
from exam_prep.oop_exam_10_apr_21.project.aquarium.saltwater_aquarium import SaltwaterAquarium
from exam_prep.oop_exam_10_apr_21.project.decoration.decoration_repository import DecorationRepository
from exam_prep.oop_exam_10_apr_21.project.decoration.ornament import Ornament
from exam_prep.oop_exam_10_apr_21.project.decoration.plant import Plant
from exam_prep.oop_exam_10_apr_21.project.fish.freshwater_fish import FreshwaterFish
from exam_prep.oop_exam_10_apr_21.project.fish.saltwater_fish import SaltwaterFish


class Controller:
    AQUARIUM_TYPES_REF = {
        'FreshwaterAquarium': FreshwaterAquarium,
        'SaltwaterAquarium': SaltwaterAquarium
    }
    DECORATION_TYPES_REF = {
        'Ornament': Ornament,
        'Plant': Plant
    }
    FISH_TYPES_REF = {
        'FreshwaterFish': FreshwaterFish,
        "SaltwaterFish": SaltwaterFish,
    }

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []  # all aquariums (objects).

    def __find_aquarium(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in Controller.AQUARIUM_TYPES_REF:
            return "Invalid aquarium type."
        new_aquarium = Controller.AQUARIUM_TYPES_REF[aquarium_type](aquarium_name)
        self.aquariums.append(new_aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        if decoration_type not in Controller.DECORATION_TYPES_REF:
            return "Invalid decoration type."
        decoration = Controller.DECORATION_TYPES_REF[decoration_type]()
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration == 'None':
            return f"There isn't a decoration of type {decoration_type}."
        aquarium = self.__find_aquarium(aquarium_name)
        if aquarium:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in Controller.FISH_TYPES_REF:
            return f"There isn't a fish of type {fish_type}."

        aquarium = self.__find_aquarium(aquarium_name)
        if not aquarium:
            return

        if aquarium.capacity == len(aquarium.fish):
            return 'Not enough capacity.'

        if (fish_type == 'FreshwaterFish' and type(aquarium).__name__ != 'FreshwaterAquarium') or \
                (fish_type == 'SaltwaterFish' and type(aquarium).__name__ != 'SaltwaterAquarium'):
            return "Water not suitable."

        fish = Controller.FISH_TYPES_REF[fish_type](fish_name, fish_species, price)
        aquarium.add_fish(fish)
        return f"Successfully added {fish_type} to {aquarium_name}."

    def feed_fish(self, aquarium_name):
        aquarium = self.__find_aquarium(aquarium_name)
        if not aquarium:
            return

        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__find_aquarium(aquarium_name)
        if not aquarium:
            return
        total_fish_value = sum(f.price for f in aquarium.fish)
        total_decorations_value = sum(d.price for d in aquarium.decorations)
        return f"The value of Aquarium {aquarium_name} is {total_fish_value + total_decorations_value:.2f}."

    def report(self):
        return '\n'.join([str(a) for a in self.aquariums])


# app = Controller()
# print(app.add_decoration('Ornament'))
# print(app.add_aquarium('FreshwaterAquarium', 'Fresh'))
# print(app.insert_decoration('Fresh', 'Ornament'))
# print(app.add_fish('Fresh', 'FreshwaterFish', 'Jorkata', 'shark', 2.2))
# print(app.feed_fish('Fresh'))