from exam_prep.oop_exam_22_aug_20.project.appliances.appliance import Appliance


class Fridge(Appliance):
    INITIAL_COST = 1.2

    def __init__(self):
        super().__init__(Fridge.INITIAL_COST)

