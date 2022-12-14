from exam_prep.oop_exam_14_aug_22.project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        increase = 2
        if self.speed + increase <= Appaloosa.MAX_SPEED:
            self.speed += increase
        else:
            self.speed = Appaloosa.MAX_SPEED