from exam_prep.oop_exam_22_aug_20.project.appliances.appliance import Appliance


class Stove(Appliance):
    INITIAL_COST = 0.7

    def __init__(self):
        super().__init__(Stove.INITIAL_COST)
