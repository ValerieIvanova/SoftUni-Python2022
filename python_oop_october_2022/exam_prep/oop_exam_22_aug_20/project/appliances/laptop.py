from exam_prep.oop_exam_22_aug_20.project.appliances.appliance import Appliance


class Laptop(Appliance):
    INITIAL_COST = 1

    def __init__(self):
        super().__init__(Laptop.INITIAL_COST)