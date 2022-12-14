from exam_prep.oop_exam_22_aug_20.project.appliances.appliance import Appliance


class TV(Appliance):
    INITIAL_COST = 1.5

    def __init__(self):
        super().__init__(TV.INITIAL_COST)
