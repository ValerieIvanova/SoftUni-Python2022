from abc import ABC, abstractmethod


class Astronaut(ABC):
    OXYGEN_FOR_BREATH = 10

    @abstractmethod
    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= self.OXYGEN_FOR_BREATH

    def increase_oxygen(self, amount):
        self.oxygen += amount