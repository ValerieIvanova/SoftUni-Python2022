from exam_prep.oop_exam_23_aug_21.project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    OXYGEN_FOR_BREATH = 5
    OXYGEN_UNITS = 70

    def __init__(self, name):
        super().__init__(name, self.OXYGEN_UNITS)