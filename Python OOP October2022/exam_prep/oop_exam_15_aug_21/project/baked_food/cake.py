from exam_prep.oop_exam_15_aug_21.project.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    PORTION = 245

    def __init__(self, name, price):
        super().__init__(name, Cake.PORTION, price)
