from exam_prep.oop_exam_11_dec_21.project.car.car import Car


class Driver:
    def __init__(self, name):
        self.name = name
        self.car: Car = None
        self.number_of_wins = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Name should contain at least one character!")
        self.__name = value
