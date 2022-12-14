from abc import ABC, abstractmethod

from exam_prep.oop_exam_10_apr_21.project.fish.freshwater_fish import FreshwaterFish
from exam_prep.oop_exam_10_apr_21.project.fish.saltwater_fish import SaltwaterFish


class BaseAquarium(ABC):
    FISH_TYPES_REF = {
        'FreshwaterFish': FreshwaterFish,
        'SaltwaterFish': SaltwaterFish,
    }

    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []  # all the decorations (objects).
        self.fish = []  # contain all the fish (objects).

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        result = sum(d.comfort for d in self.decorations)
        return result

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."
        fish_type = fish.__class__.__name__
        if fish_type not in ('FreshwaterFish', 'SaltwaterFish'):
            return

        self.fish.append(fish)
        return f"Successfully added {fish_type} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        [f.eat() for f in self.fish]

    def __str__(self):
        result = [f"{self.name}:",
                  f"Fish: {' '.join(f.name for f in self.fish)}" if self.fish else 'Fish: none',
                  f"Decorations: {len(self.decorations)}",
                  f"Comfort: {self.calculate_comfort()}"
                  ]
        return '\n'.join(result)
