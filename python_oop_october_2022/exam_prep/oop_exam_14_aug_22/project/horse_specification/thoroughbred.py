from exam_prep.oop_exam_14_aug_22.project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        increase = 3
        if self.speed + increase <= Thoroughbred.MAX_SPEED:
            self.speed += increase
        else:
            self.speed = Thoroughbred.MAX_SPEED